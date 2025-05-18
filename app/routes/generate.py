from fastapi import APIRouter, HTTPException
from app.schemas import GenerateNoteRequest, GenerateNoteResponse, SOAPNote
from app.services.gpt_service import generate_soap_note, generate_polished_note
from app.mock_db import db
from app.utils.logger import log_request

router = APIRouter()

@router.post("/generate_note", response_model=GenerateNoteResponse)
@log_request
async def generate_note(request: GenerateNoteRequest):
    try:
        # Generate SOAP note
        soap_note = await generate_soap_note(
            transcript=request.transcript,
            patient_age=request.patient_age,
            visit_type=request.visit_type,
            provider_notes=request.provider_notes
        )
        
        # Generate polished note
        polished_note = await generate_polished_note(soap_note)
        
        # Create response
        response = GenerateNoteResponse(
            soap_note=soap_note,
            polished_note=polished_note,
            visit_id=""  # Will be set by store_visit
        )
        
        # Store in mock DB and get visit ID
        response.visit_id = db.store_visit(response)
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 