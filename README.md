# Syntera Backend

AI medical scribe backend service for pediatricians, featuring automatic transcription and SOAP note generation.

## Features

- Audio transcription using OpenAI's Whisper
- SOAP note generation (coming soon with GPT-4 + RAG)
- FastAPI-based REST API
- CORS-enabled for frontend integration

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
# Make sure you're in the backend directory
PYTHONPATH=$PYTHONPATH:./app uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### POST /transcribe
Upload an audio file for transcription using Whisper.

### POST /generate_soap
Generate a SOAP note from a transcript (placeholder endpoint).

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development

The project structure is organized as follows:
```
backend/
├── app/
│   ├── routers/
│   │   ├── transcribe.py
│   │   └── soap.py
│   ├── services/
│   │   └── transcription_service.py
│   ├── models.py
│   └── main.py
└── requirements.txt
``` 