from src.modules._base.schema import BaseEntryCreate, BaseEntryRead

class GoodDeedEntryCreate(BaseEntryCreate):
    title: str
    description: str | None = None
    tags: str | None = None

class GoodDeedEntryRead(BaseEntryRead):
    title: str
    description: str | None
    tags: str | None
