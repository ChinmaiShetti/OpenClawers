from src.modules._base.router import make_crud_router
from src.modules.good_deeds.model import GoodDeedEntry
from src.modules.good_deeds.schema import GoodDeedEntryCreate, GoodDeedEntryRead

router = make_crud_router(
    model=GoodDeedEntry,
    create_schema=GoodDeedEntryCreate,
    read_schema=GoodDeedEntryRead,
    module_name="good_deeds",
)
