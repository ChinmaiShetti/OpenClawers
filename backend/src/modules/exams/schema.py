from src.modules._base.schema import BaseEntryCreate, BaseEntryRead

class ExamEntryCreate(BaseEntryCreate):
    title: str
    description: str | None = None
    tags: str | None = None

class ExamEntryRead(BaseEntryRead):
    title: str
    description: str | None
    tags: str | None
