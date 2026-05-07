from src.modules._base.schema import BaseEntryCreate, BaseEntryRead
from typing import Literal

class BookEntryCreate(BaseEntryCreate):
    title: str
    author: str | None = None
    pages_read: int = 0
    notes: str | None = None
    rating: Literal[1, 2, 3, 4, 5] | None = None

class BookEntryRead(BaseEntryRead):
    title: str
    author: str | None
    pages_read: int
    notes: str | None
    rating: int | None
