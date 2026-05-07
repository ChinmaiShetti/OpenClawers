from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import settings

# SQLite needs check_same_thread=False in dev
connect_args = {"check_same_thread": False} if "sqlite" in settings.database_url else {}

engine = create_engine(settings.database_url, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
