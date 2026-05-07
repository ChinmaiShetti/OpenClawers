from sqlalchemy import Column, String, Float, Integer
from src.modules._base.model import BaseModuleModel

class BookEntry(BaseModuleModel):
    __tablename__ = "book_logs"
    title = Column(String, nullable=False)
    author = Column(String, nullable=True)
    pages_read = Column(Integer, default=0)
    notes = Column(String, nullable=True)
    rating = Column(Integer, nullable=True)   # 1-5
