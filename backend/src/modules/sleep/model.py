from sqlalchemy import Column, String, Float, Integer
from src.modules._base.model import BaseModuleModel

class SleepLog(BaseModuleModel):
    __tablename__ = "sleep_logs"
    duration_hours = Column(Float, nullable=False)
    quality = Column(Integer, nullable=False)   # 1-5
    bedtime = Column(String, nullable=True)
    wake_time = Column(String, nullable=True)
    notes = Column(String, nullable=True)
