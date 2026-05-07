from src.modules._base.schema import BaseEntryCreate, BaseEntryRead

class GameEntryCreate(BaseEntryCreate):
    title: str
    description: str | None = None
    tags: str | None = None

class GameEntryRead(BaseEntryRead):
    title: str
    description: str | None
    tags: str | None
