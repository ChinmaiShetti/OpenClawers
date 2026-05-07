from src.modules._base.router import make_crud_router
from src.modules.exams.model import ExamEntry
from src.modules.exams.schema import ExamEntryCreate, ExamEntryRead

router = make_crud_router(
    model=ExamEntry,
    create_schema=ExamEntryCreate,
    read_schema=ExamEntryRead,
    module_name="exams",
)
