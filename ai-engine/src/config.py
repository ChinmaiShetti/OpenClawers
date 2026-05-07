from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    backend_url: str = "http://localhost:8000"
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "openclaw_memories"
    anthropic_api_key: str = ""
    gemini_api_key: str = ""
    notion_token: str = ""
    slack_token: str = ""
    github_token: str = ""
    whatsapp_api_key: str = ""
    whatsapp_phone_number_id: str = ""

    class Config:
        env_file = ".env"
        extra = "ignore"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
