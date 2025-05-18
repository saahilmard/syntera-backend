from pydantic import BaseModel, Field
from typing import Optional

class GenerateNoteRequest(BaseModel):
    transcript: str = Field(..., description="Whisper-generated transcript of the visit")
    patient_age: int = Field(..., description="Patient age in months")
    visit_type: str = Field(..., description="Type of visit (e.g., 'well-child', 'sick-visit')")
    provider_notes: Optional[str] = Field(None, description="Optional additional notes from provider")

class SOAPNote(BaseModel):
    subjective: str = Field(..., description="Patient's reported symptoms and history")
    objective: str = Field(..., description="Clinical findings and measurements")
    assessment: str = Field(..., description="Diagnosis and clinical assessment")
    plan: str = Field(..., description="Treatment plan and follow-up")

class GenerateNoteResponse(BaseModel):
    soap_note: SOAPNote
    polished_note: str = Field(..., description="Narrative summary of the visit")
    visit_id: str = Field(..., description="Unique identifier for the visit")

class RegenerateRequest(BaseModel):
    soap_note: SOAPNote

class RegenerateResponse(BaseModel):
    polished_note: str = Field(..., description="New narrative summary of the visit") 