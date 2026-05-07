from typing import Generator
from src.db.session import SessionLocal


def get_db() -> Generator:
    """FastAPI dependency — yields a SQLAlchemy session and closes it after."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
