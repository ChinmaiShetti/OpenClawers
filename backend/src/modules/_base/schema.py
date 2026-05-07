"""
src/modules/_base/schema.py
────────────────────────────
Abstract Pydantic base schemas. All module schemas inherit from this.
"""
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class BaseEntryCreate(BaseModel):
    """Base schema for creating any module entry."""
    user_id: str
    # Each module adds its own fields below this


class BaseEntryRead(BaseModel):
    """Base schema for reading any module entry (includes DB-generated fields)."""
    model_config = ConfigDict(from_attributes=True)

    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime


class ModuleSummary(BaseModel):
    """Generic summary returned by GET /modules/{module}/summary"""
    module: str
    entry_count: int
    last_entry_at: datetime | None = None
    summary_data: dict = {}
