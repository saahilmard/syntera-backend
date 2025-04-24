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

## Security Notes

- Never commit the `.env` file or any files containing API keys
- The FAISS index files are excluded from git for security and size reasons
- Make sure to properly set up environment variables before running the application

## Features

- FastAPI-based REST API
- RAG pipeline for context-aware medical note generation
- PDF document processing and vectorization
- GPT-4 powered SOAP note generation
- CORS support for frontend integration

## Running the API

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```