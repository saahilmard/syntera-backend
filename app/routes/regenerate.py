from fastapi import APIRouter, HTTPException
from app.schemas import RegenerateRequest, RegenerateResponse
from app.services.gpt_service import generate_polished_note
from app.utils.logger import log_request

router = APIRouter()

@router.post("/regenerate", response_model=RegenerateResponse)
@log_request
async def regenerate_note(request: RegenerateRequest):
    try:
        # Generate new polished note
        polished_note = await generate_polished_note(request.soap_note)
        
        return RegenerateResponse(polished_note=polished_note)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 