# Syntera API - AI Medical Scribe Backend

This is the backend API for Syntera, an AI-powered medical scribe system that generates SOAP notes using RAG (Retrieval-Augmented Generation) with pediatric medical knowledge.

## Features

- FastAPI-based REST API
- RAG pipeline for context-aware medical note generation
- PDF document processing and vectorization
- GPT-4 powered SOAP note generation
- CORS support for frontend integration

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with:
```
OPENAI_API_KEY=your_openai_api_key_here
```

5. Add pediatric medical PDFs:
- Place your pediatric medical PDFs in `rag_pipeline/rag_docs/`
- Initialize the vector store:
```bash
python -m app.rag_pipeline.load_pediatric_pdfs
```

## Running the API

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Generate SOAP Notes
- **POST** `/generate_soap`
- Request body:
```json
{
    "transcript": "patient conversation transcript",
    "patient_age": 5,
    "visit_type": "well-child"
}
```

## Project Structure

```
backend/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── rag_pipeline/
│   │   ├── load_pediatric_pdfs.py
│   │   ├── query_rag_context.py
│   │   ├── rag.py
│   │   └── rag_docs/
│   └── routers/
│       ├── soap.py
│       └── transcribe.py
├── requirements.txt
└── README.md
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 