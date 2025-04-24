import whisper
import tempfile
import os
from fastapi import UploadFile
import time

# Load Whisper model globally
model = whisper.load_model("base")

async def transcribe_audio(audio: UploadFile) -> tuple[str, float]:
    """
    Transcribe audio using Whisper
    Returns tuple of (transcription text, duration in seconds)
    """
    # Create temporary file to store uploaded audio
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio.filename)[1]) as temp_file:
        # Write uploaded file to temp file
        content = await audio.read()
        temp_file.write(content)
        temp_file.flush()
        
        start_time = time.time()
        
        # Transcribe using Whisper
        result = model.transcribe(temp_file.name)
        
        duration = time.time() - start_time
        
        # Clean up temp file
        os.unlink(temp_file.name)
        
        return result["text"].strip(), duration
