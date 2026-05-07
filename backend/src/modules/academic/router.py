from src.modules._base.router import make_crud_router
from src.modules.academic.model import AcademicEntry
from src.modules.academic.schema import AcademicEntryCreate, AcademicEntryRead

router = make_crud_router(
    model=AcademicEntry, create_schema=AcademicEntryCreate, read_schema=AcademicEntryRead, module_name="academic"
)
