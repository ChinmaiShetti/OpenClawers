from sqlalchemy import Column, String, Float, Integer
from src.modules._base.model import BaseModuleModel

class WorkoutLog(BaseModuleModel):
    __tablename__ = "fitness_logs"
    type = Column(String, nullable=False)          # workout | food | body_metric
    workout_type = Column(String, nullable=True)
    duration_minutes = Column(Integer, nullable=True)
    calories = Column(Float, nullable=True)
    weight_kg = Column(Float, nullable=True)
    notes = Column(String, nullable=True)
