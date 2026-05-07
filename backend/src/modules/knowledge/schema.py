from src.modules._base.schema import BaseEntryCreate, BaseEntryRead

class KnowledgeEntryCreate(BaseEntryCreate):
    title: str
    description: str | None = None
    tags: str | None = None

class KnowledgeEntryRead(BaseEntryRead):
    title: str
    description: str | None
    tags: str | None
