from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import transcribe, soap

app = FastAPI(title="Syntera API", description="Backend API for Syntera - AI Medical Scribe")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(transcribe.router, tags=["transcribe"])
app.include_router(soap.router, tags=["soap"])

@app.get("/")
async def root():
    return {"message": "Welcome to Syntera API"}
