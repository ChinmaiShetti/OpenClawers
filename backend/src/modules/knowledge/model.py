from sqlalchemy import Column, String, Text
from src.modules._base.model import BaseModuleModel

class KnowledgeEntry(BaseModuleModel):
    __tablename__ = "knowledge_logs"
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    tags = Column(String, nullable=True)   # comma-separated
