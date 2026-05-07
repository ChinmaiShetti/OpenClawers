from fastapi import APIRouter
from pydantic import BaseModel
from src.priority_engine.engine import compute_priority

router = APIRouter()

class PriorityRequest(BaseModel):
    user_id: str = "demo-user"

@router.post("/compute")
async def compute(req: PriorityRequest):
    """POST /priority/compute → returns ranked focus list."""
    items = await compute_priority(req.user_id)
    return {"data": items}
