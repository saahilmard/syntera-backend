# Syntera Backend

Backend API for Syntera - AI Medical Scribe

## Setup

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with the following variables:
```
OPENAI_API_KEY=your_api_key_here
```

## RAG Pipeline

The RAG (Retrieval Augmented Generation) pipeline is located in `app/rag_pipeline/`. It uses FAISS for vector storage and retrieval of medical knowledge. The vector store files are not included in the repository and need to be generated locally.

### Testing the RAG Pipeline

You can test the RAG pipeline using:
```bash
python app/rag_pipeline/test_rag.py
```

## Running the API

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## API Endpoints

### Generate SOAP Note
```bash
curl -X POST http://localhost:8000/api/generate_note \
  -H "Content-Type: application/json" \
  -d '{
    "transcript": "Patient presents with fever and cough for 3 days. Temperature 101.2F. Lungs clear to auscultation.",
    "patient_age": 24,
    "visit_type": "sick-visit",
    "provider_notes": "No recent travel, no known COVID exposure"
  }'
```

### Regenerate Polished Note
```bash
curl -X POST http://localhost:8000/api/regenerate \
  -H "Content-Type: application/json" \
  -d '{
    "soap_note": {
      "subjective": "3-day history of fever and cough",
      "objective": "Temp 101.2F, lungs clear",
      "assessment": "Acute viral URI",
      "plan": "Supportive care, follow up if worsening"
    }
  }'
```

## Features

- FastAPI-based REST API
- RAG pipeline for context-aware medical note generation
- PDF document processing and vectorization
- GPT-4 powered SOAP note generation
- CORS support for frontend integration
- Health check endpoint
- Mock data storage

## Security Notes

- This is a demo application using mock data
- All data is stored in-memory and is not persistent
- API keys should be kept secure and never committed to version control