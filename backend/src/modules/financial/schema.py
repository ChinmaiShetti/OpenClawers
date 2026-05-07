from pydantic import BaseModel
from typing import Literal
from src.modules._base.schema import BaseEntryCreate, BaseEntryRead

class TransactionCreate(BaseEntryCreate):
    type: Literal["income", "expense", "savings"]
    amount: float
    currency: str = "INR"
    category: str
    description: str | None = None

class TransactionRead(BaseEntryRead):
    type: str
    amount: float
    currency: str
    category: str
    description: str | None
