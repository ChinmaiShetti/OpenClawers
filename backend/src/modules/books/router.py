from src.modules._base.router import make_crud_router
from src.modules.books.model import BookEntry
from src.modules.books.schema import BookEntryCreate, BookEntryRead

router = make_crud_router(
    model=BookEntry, create_schema=BookEntryCreate, read_schema=BookEntryRead, module_name="books"
)
