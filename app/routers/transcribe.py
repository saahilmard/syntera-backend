from fastapi import APIRouter, UploadFile, File
from services.transcription_service import transcribe_audio
from models import TranscriptionResponse

router = APIRouter()

@router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio_file(audio: UploadFile = File(...)):
    """
    Transcribe an audio file using Whisper
    """
    text, duration = await transcribe_audio(audio)
    return TranscriptionResponse(text=text, duration=duration)
