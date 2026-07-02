"""
Prediction service.

Approach:
- We generate small synthetic training data from each condition's
  "typical_symptoms" list (random subsets + a little noise), turn it into
  multi-hot feature vectors, and train a Naive Bayes classifier.
- This is a lightweight, explainable stand-in for a real ML pipeline.
  It demonstrates the architecture (vectorize -> model -> predict) without
  requiring a real clinical dataset, which this project does not have.
- For a production system, this entire module would need to be replaced
  with a model trained and validated on real, licensed medical data,
  under clinical supervision.
"""

import random
from typing import List, Tuple

import numpy as np
from sklearn.naive_bayes import BernoulliNB

from app.data.conditions import CONDITIONS, SYMPTOM_VOCAB

random.seed(42)
np.random.seed(42)

SYMPTOM_INDEX = {s: i for i, s in enumerate(SYMPTOM_VOCAB)}
CONDITION_NAMES = list(CONDITIONS.keys())


def _vectorize(symptoms: List[str]) -> np.ndarray:
    vec = np.zeros(len(SYMPTOM_VOCAB), dtype=int)
    for s in symptoms:
        if s in SYMPTOM_INDEX:
            vec[SYMPTOM_INDEX[s]] = 1
    return vec


def _generate_training_data(samples_per_condition: int = 60) -> Tuple[np.ndarray, np.ndarray]:
    X, y = [], []
    all_symptoms = SYMPTOM_VOCAB

    for label, cond in CONDITIONS.items():
        typical = cond["typical_symptoms"]
        for _ in range(samples_per_condition):
            # Pick a random subset of the condition's typical symptoms
            # (simulates that not every patient has every symptom).
            k = random.randint(max(1, len(typical) // 2), len(typical))
            chosen = set(random.sample(typical, k))

            # Add a little noise: small chance of an unrelated symptom.
            if random.random() < 0.15:
                chosen.add(random.choice(all_symptoms))

            X.append(_vectorize(list(chosen)))
            y.append(label)

    return np.array(X), np.array(y)


class SymptomPredictor:
    def __init__(self):
        X, y = _generate_training_data()
        self.model = BernoulliNB()
        self.model.fit(X, y)

    def predict(self, symptoms: List[str], top_n: int = 5):
        known = [s for s in symptoms if s in SYMPTOM_INDEX]
        unknown = [s for s in symptoms if s not in SYMPTOM_INDEX]

        if not known:
            return [], unknown

        vec = _vectorize(known).reshape(1, -1)
        probs = self.model.predict_proba(vec)[0]
        class_order = self.model.classes_

        ranked = sorted(zip(class_order, probs), key=lambda x: x[1], reverse=True)[:top_n]

        results = []
        for name, prob in ranked:
            cond = CONDITIONS[name]
            results.append({
                "name": name,
                "confidence": round(float(prob), 3),
                "urgent": cond["urgent"],
                "home_care": cond["home_care"],
                "see_doctor_if": cond["see_doctor_if"],
            })

        return results, unknown


# Single shared instance (model is small/cheap to train at startup).
predictor = SymptomPredictor()
