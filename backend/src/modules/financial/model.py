from sqlalchemy import Column, String, Float, Enum
from src.modules._base.model import BaseModuleModel
import enum

class TransactionType(str, enum.Enum):
    income = "income"
    expense = "expense"
    savings = "savings"

class Transaction(BaseModuleModel):
    __tablename__ = "financial_transactions"
    type = Column(Enum(TransactionType), nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, default="INR")
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
