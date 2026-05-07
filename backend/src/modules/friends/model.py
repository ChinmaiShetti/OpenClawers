from sqlalchemy import Column, String, Text
from src.modules._base.model import BaseModuleModel

class FriendEntry(BaseModuleModel):
    __tablename__ = "friends_logs"
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    tags = Column(String, nullable=True)   # comma-separated
