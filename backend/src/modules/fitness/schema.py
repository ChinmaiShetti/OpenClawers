from src.modules._base.schema import BaseEntryCreate, BaseEntryRead
from typing import Literal

class WorkoutLogCreate(BaseEntryCreate):
    type: Literal["workout", "food", "body_metric"]
    workout_type: str | None = None
    duration_minutes: int | None = None
    calories: float | None = None
    weight_kg: float | None = None
    notes: str | None = None

class WorkoutLogRead(BaseEntryRead):
    type: str
    workout_type: str | None
    duration_minutes: int | None
    calories: float | None
    weight_kg: float | None
    notes: str | None
