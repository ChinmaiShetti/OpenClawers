from src.modules._base.schema import BaseEntryCreate, BaseEntryRead

class FriendEntryCreate(BaseEntryCreate):
    title: str
    description: str | None = None
    tags: str | None = None

class FriendEntryRead(BaseEntryRead):
    title: str
    description: str | None
    tags: str | None
