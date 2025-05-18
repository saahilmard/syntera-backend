from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str = ""  # Your OpenAI API key here
    OPENAI_ORG_ID: str = ""   # Your OpenAI organization ID here
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 