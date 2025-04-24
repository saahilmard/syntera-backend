from fastapi import APIRouter
from models import SOAPResponse

router = APIRouter()

@router.post("/generate_soap", response_model=SOAPResponse)
async def generate_soap_note(transcript: str):
    """
    Generate SOAP note from transcript (placeholder)
    """
    # Placeholder response until GPT-4 + RAG implementation
    return SOAPResponse(
        subjective="Placeholder subjective note",
        objective="Placeholder objective note",
        assessment="Placeholder assessment",
        plan="Placeholder plan"
    )
