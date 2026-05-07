"""
src/modules/_base/model.py
─────────────────────────
Abstract ORM base model. All module models inherit from this.
Provides: id, user_id, created_at, updated_at.
"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from src.db.base import Base


class BaseModuleModel(Base):
    """Abstract base — do NOT use directly in tables."""
    __abstract__ = True

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
