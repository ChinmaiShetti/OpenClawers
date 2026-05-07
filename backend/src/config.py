from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    database_url: str = "sqlite:///./openclaw.db"
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "openclaw_memories"
    openai_api_key: str = ""
    jwt_secret: str = "dev-secret-change-me"

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
