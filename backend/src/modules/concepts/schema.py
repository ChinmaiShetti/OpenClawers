from src.modules._base.schema import BaseEntryCreate, BaseEntryRead

class ConceptEntryCreate(BaseEntryCreate):
    title: str
    description: str | None = None
    tags: str | None = None

class ConceptEntryRead(BaseEntryRead):
    title: str
    description: str | None
    tags: str | None
