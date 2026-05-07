from src.modules._base.router import make_crud_router
from src.modules.friends.model import FriendEntry
from src.modules.friends.schema import FriendEntryCreate, FriendEntryRead

router = make_crud_router(
    model=FriendEntry,
    create_schema=FriendEntryCreate,
    read_schema=FriendEntryRead,
    module_name="friends",
)
