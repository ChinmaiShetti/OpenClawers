from src.modules._base.router import make_crud_router
from src.modules.fitness.model import WorkoutLog
from src.modules.fitness.schema import WorkoutLogCreate, WorkoutLogRead

router = make_crud_router(
    model=WorkoutLog,
    create_schema=WorkoutLogCreate,
    read_schema=WorkoutLogRead,
    module_name="fitness",
)
