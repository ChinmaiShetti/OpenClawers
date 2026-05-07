from src.modules._base.schema import BaseEntryCreate, BaseEntryRead
from typing import Literal

class AcademicEntryCreate(BaseEntryCreate):
    entry_type: Literal["course", "assignment", "grade"]
    course_name: str
    score: float | None = None
    max_score: float | None = None
    description: str | None = None

class AcademicEntryRead(BaseEntryRead):
    entry_type: str
    course_name: str
    score: float | None
    max_score: float | None
    description: str | None
