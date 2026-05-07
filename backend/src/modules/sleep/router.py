from src.modules._base.router import make_crud_router
from src.modules.sleep.model import SleepLog
from src.modules.sleep.schema import SleepLogCreate, SleepLogRead

router = make_crud_router(
    model=SleepLog,
    create_schema=SleepLogCreate,
    read_schema=SleepLogRead,
    module_name="sleep",
)
