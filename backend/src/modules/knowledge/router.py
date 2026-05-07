from src.modules._base.router import make_crud_router
from src.modules.knowledge.model import KnowledgeEntry
from src.modules.knowledge.schema import KnowledgeEntryCreate, KnowledgeEntryRead

router = make_crud_router(
    model=KnowledgeEntry,
    create_schema=KnowledgeEntryCreate,
    read_schema=KnowledgeEntryRead,
    module_name="knowledge",
)
