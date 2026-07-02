"""
Small demo knowledge base mapping conditions to their typical symptoms
and safe, general guidance.

IMPORTANT: This is hand-written sample data for an educational demo.
It is NOT clinically validated. A real system needs a licensed medical
professional to build and review the dataset before any real-world use.
"""

# The full list of symptoms the system knows about (used to build the
# feature vector for the ML model).
SYMPTOM_VOCAB = [
    "fever", "cough", "sore_throat", "runny_nose", "headache", "body_ache",
    "fatigue", "nausea", "vomiting", "diarrhea", "stomach_pain", "chest_pain",
    "shortness_of_breath", "dizziness", "rash", "joint_pain", "sneezing",
    "loss_of_appetite", "chills", "sensitivity_to_light", "itchy_eyes",
    "congestion",
]

# Each condition: typical symptoms (used to generate training data),
# plus the guidance shown to the user.
CONDITIONS = {
    "Common Cold": {
        "typical_symptoms": ["runny_nose", "sneezing", "sore_throat", "cough", "congestion", "headache"],
        "urgent": False,
        "home_care": (
            "Rest, drink warm fluids (water, herbal tea, warm soup), gargle with "
            "warm salt water for a sore throat, and use a humidifier if the air is "
            "dry. Honey in warm water can soothe a cough (avoid honey for children "
            "under 1 year)."
        ),
        "see_doctor_if": "Symptoms last more than 10 days, or you develop a high fever or trouble breathing.",
    },
    "Seasonal Flu": {
        "typical_symptoms": ["fever", "body_ache", "chills", "fatigue", "headache", "cough", "sore_throat"],
        "urgent": False,
        "home_care": (
            "Rest as much as possible, stay well hydrated, and keep warm. A "
            "lukewarm sponge can help with fever discomfort. Light, easy-to-digest "
            "food (broth, plain rice) is often better tolerated than heavy meals."
        ),
        "see_doctor_if": "Fever is high or lasts more than 3 days, or you have difficulty breathing, chest pain, or confusion — these need urgent medical attention.",
    },
    "Migraine / Tension Headache": {
        "typical_symptoms": ["headache", "sensitivity_to_light", "nausea", "dizziness"],
        "urgent": False,
        "home_care": (
            "Rest in a quiet, dark room, apply a cool or warm compress to your "
            "head/neck, stay hydrated, and try gentle neck stretches. Limiting "
            "screen time can also help."
        ),
        "see_doctor_if": "This is 'the worst headache of your life', comes on suddenly and severely, or is paired with confusion, vision changes, or slurred speech — seek emergency care immediately.",
    },
    "Food Poisoning / Stomach Upset": {
        "typical_symptoms": ["nausea", "vomiting", "diarrhea", "stomach_pain", "loss_of_appetite"],
        "urgent": False,
        "home_care": (
            "Sip clear fluids frequently (water, oral rehydration solution, "
            "coconut water) to avoid dehydration. Eat bland food when ready (rice, "
            "banana, toast). Ginger tea can help settle nausea. Avoid dairy, "
            "caffeine, and spicy/fatty food until you feel better."
        ),
        "see_doctor_if": "You see blood in vomit or stool, can't keep fluids down, show signs of dehydration (very dark urine, dizziness), or symptoms last more than 2 days.",
    },
    "Allergic Reaction / Hay Fever": {
        "typical_symptoms": ["sneezing", "runny_nose", "rash", "itchy_eyes", "sensitivity_to_light"],
        "urgent": False,
        "home_care": (
            "Try to identify and avoid the trigger (dust, pollen, certain foods), "
            "rinse your nose/eyes with clean water, and keep your living space "
            "clean and well-ventilated."
        ),
        "see_doctor_if": "You notice swelling of the face/lips/throat, difficulty breathing, or widespread hives — this can be a medical emergency (possible anaphylaxis).",
    },
    "Possible Respiratory Infection": {
        "typical_symptoms": ["cough", "fever", "shortness_of_breath", "chest_pain", "fatigue"],
        "urgent": True,
        "home_care": "Rest and stay hydrated while you arrange to be seen — this symptom combination should not be managed with home care alone.",
        "see_doctor_if": "Please see a doctor promptly. Shortness of breath combined with fever/cough/chest pain can indicate a more serious infection (e.g. pneumonia) that needs proper evaluation, possibly urgently.",
    },
    "Possible Cardiac Concern": {
        "typical_symptoms": ["chest_pain", "shortness_of_breath", "dizziness"],
        "urgent": True,
        "home_care": "No home remedy is appropriate here.",
        "see_doctor_if": "Chest pain with shortness of breath or dizziness can be a sign of a heart-related emergency. Seek emergency medical care immediately or call your local emergency number — do not wait or try to self-treat.",
    },
    "Joint / Body Inflammation": {
        "typical_symptoms": ["joint_pain", "fatigue", "fever", "body_ache"],
        "urgent": False,
        "home_care": (
            "Rest the affected area, apply a cold pack for swelling or a warm "
            "compress for stiffness, and stay gently active within comfort."
        ),
        "see_doctor_if": "Joints are visibly swollen, red, or hot to the touch, or pain persists beyond a week.",
    },
}
