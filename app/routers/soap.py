from fastapi import APIRouter
from pydantic import BaseModel
from app.models import SOAPResponse
from app.rag_pipeline.rag import generate_soap_notes

router = APIRouter()

class SOAPRequest(BaseModel):
    transcript: str
    patient_age: int
    visit_type: str

@router.post("/generate_soap", response_model=SOAPResponse)
async def generate_soap_note(request: SOAPRequest):
    """
    Generate SOAP note using RAG-enhanced GPT-4
    """
    soap_note = generate_soap_notes(
        transcription=request.transcript,
        patient_age=request.patient_age,
        visit_type=request.visit_type
    )
    
    # Parse the response into sections (assuming the model returns properly formatted sections)
    sections = soap_note.split("\n\n")
    soap_dict = {}
    
    for section in sections:
        if section.startswith("S:"):
            soap_dict["subjective"] = section[2:].strip()
        elif section.startswith("O:"):
            soap_dict["objective"] = section[2:].strip()
        elif section.startswith("A:"):
            soap_dict["assessment"] = section[2:].strip()
        elif section.startswith("P:"):
            soap_dict["plan"] = section[2:].strip()
    
    return SOAPResponse(**soap_dict)
