from src.modules._base.router import make_crud_router
from src.modules.games.model import GameEntry
from src.modules.games.schema import GameEntryCreate, GameEntryRead

router = make_crud_router(
    model=GameEntry,
    create_schema=GameEntryCreate,
    read_schema=GameEntryRead,
    module_name="games",
)
