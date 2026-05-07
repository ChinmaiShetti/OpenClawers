from fastapi import APIRouter, Query
from pydantic import BaseModel
from src.reflection.generator import generate_reflection

router = APIRouter()

class ReflectionRequest(BaseModel):
    user_id: str = "demo-user"

@router.post("/generate")
async def generate(
    req: ReflectionRequest,
    period: str = Query("daily", regex="^(daily|weekly|monthly|annual)$"),
):
    """POST /reflection/generate?period=daily"""
    result = await generate_reflection(period, req.user_id)
    return {"data": result}
