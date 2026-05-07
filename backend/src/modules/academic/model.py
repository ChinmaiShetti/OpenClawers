from sqlalchemy import Column, String, Float, Integer
from src.modules._base.model import BaseModuleModel

class AcademicEntry(BaseModuleModel):
    __tablename__ = "academic_logs"
    entry_type = Column(String, nullable=False)   # course | assignment | grade
    course_name = Column(String, nullable=False)
    score = Column(Float, nullable=True)
    max_score = Column(Float, nullable=True)
    description = Column(String, nullable=True)
