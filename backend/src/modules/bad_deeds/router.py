from src.modules._base.router import make_crud_router
from src.modules.bad_deeds.model import BadDeedEntry
from src.modules.bad_deeds.schema import BadDeedEntryCreate, BadDeedEntryRead

router = make_crud_router(
    model=BadDeedEntry,
    create_schema=BadDeedEntryCreate,
    read_schema=BadDeedEntryRead,
    module_name="bad_deeds",
)
