from typing import List
from pydantic import BaseModel, Field


class SymptomRequest(BaseModel):
    symptoms: List[str] = Field(
        ..., description="List of symptom keys, e.g. ['fever', 'cough']"
    )


class ConditionResult(BaseModel):
    name: str
    confidence: float
    urgent: bool
    home_care: str
    see_doctor_if: str


class SymptomResponse(BaseModel):
    input_symptoms: List[str]
    unknown_symptoms: List[str]
    results: List[ConditionResult]
    any_urgent: bool
    disclaimer: str = (
        "This tool provides general educational information only. It is not a "
        "medical diagnosis and cannot replace a qualified healthcare "
        "professional. If you are seriously concerned about your health, seek "
        "medical care."
    )


class SymptomVocabResponse(BaseModel):
    symptoms: List[str]
