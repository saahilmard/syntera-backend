from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import generate, regenerate
from app.utils.logger import logger

app = FastAPI(title="Syntera AI Scribe API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(generate.router, prefix="/api/v1", tags=["SOAP Note Generation"])
app.include_router(regenerate.router, prefix="/api/v1", tags=["SOAP Note Regeneration"])

@app.get("/")
async def root():
    return {"message": "Welcome to Syntera AI Scribe API"}

@app.get("/ping")
async def ping():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Syntera API is running"}

@app.get("/")
async def root():
    """Root endpoint with demo warning"""
    logger.warning("This is a demo application. All data is mock data.")
    return {
        "message": "Welcome to Syntera API",
        "warning": "This is a demo application. All data is mock data."
    }
