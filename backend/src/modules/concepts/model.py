from sqlalchemy import Column, String, Text
from src.modules._base.model import BaseModuleModel

class ConceptEntry(BaseModuleModel):
    __tablename__ = "concepts_logs"
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    tags = Column(String, nullable=True)   # comma-separated
