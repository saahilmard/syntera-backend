from pydantic import BaseModel
from typing import Optional

class TranscriptionResponse(BaseModel):
    text: str
    duration: float
    
class SOAPResponse(BaseModel):
    """
    Pydantic model for SOAP note response
    """
    subjective: str
    objective: str
    assessment: str
    plan: str
