from sqlalchemy import Column, String, Text
from src.modules._base.model import BaseModuleModel

class GoodDeedEntry(BaseModuleModel):
    __tablename__ = "good_deeds_logs"
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    tags = Column(String, nullable=True)   # comma-separated
