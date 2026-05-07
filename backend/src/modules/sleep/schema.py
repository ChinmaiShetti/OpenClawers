from src.modules._base.schema import BaseEntryCreate, BaseEntryRead
from typing import Literal

class SleepLogCreate(BaseEntryCreate):
    duration_hours: float
    quality: Literal[1, 2, 3, 4, 5]
    bedtime: str | None = None
    wake_time: str | None = None
    notes: str | None = None

class SleepLogRead(BaseEntryRead):
    duration_hours: float
    quality: int
    bedtime: str | None
    wake_time: str | None
    notes: str | None
