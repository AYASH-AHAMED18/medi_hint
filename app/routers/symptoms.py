from fastapi import APIRouter

from app.data.conditions import SYMPTOM_VOCAB
from app.models.schemas import SymptomRequest, SymptomResponse, SymptomVocabResponse
from app.services.predictor import predictor

router = APIRouter(prefix="/api", tags=["symptoms"])


@router.get("/symptoms", response_model=SymptomVocabResponse)
def get_known_symptoms():
    """Returns the list of symptom keys the system understands."""
    return SymptomVocabResponse(symptoms=SYMPTOM_VOCAB)


@router.post("/predict", response_model=SymptomResponse)
def predict_conditions(payload: SymptomRequest):
    """
    Given a list of symptoms, returns up to 5 possible conditions with
    confidence scores, general home-care guidance, and a doctor-referral
    flag. This is educational information, not a diagnosis.
    """
    results, unknown = predictor.predict(payload.symptoms)
    any_urgent = any(r["urgent"] for r in results)

    return SymptomResponse(
        input_symptoms=payload.symptoms,
        unknown_symptoms=unknown,
        results=results,
        any_urgent=any_urgent,
    )
