from src.modules._base.router import make_crud_router
from src.modules.financial.model import Transaction
from src.modules.financial.schema import TransactionCreate, TransactionRead

router = make_crud_router(
    model=Transaction,
    create_schema=TransactionCreate,
    read_schema=TransactionRead,
    module_name="financial",
)
