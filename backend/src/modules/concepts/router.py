from src.modules._base.router import make_crud_router
from src.modules.concepts.model import ConceptEntry
from src.modules.concepts.schema import ConceptEntryCreate, ConceptEntryRead

router = make_crud_router(
    model=ConceptEntry,
    create_schema=ConceptEntryCreate,
    read_schema=ConceptEntryRead,
    module_name="concepts",
)
