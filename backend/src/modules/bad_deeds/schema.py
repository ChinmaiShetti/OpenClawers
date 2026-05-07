from src.modules._base.schema import BaseEntryCreate, BaseEntryRead

class BadDeedEntryCreate(BaseEntryCreate):
    title: str
    description: str | None = None
    tags: str | None = None

class BadDeedEntryRead(BaseEntryRead):
    title: str
    description: str | None
    tags: str | None
