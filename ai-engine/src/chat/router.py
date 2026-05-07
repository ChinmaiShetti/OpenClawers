from fastapi import APIRouter
from pydantic import BaseModel
from src.chat.handler import handle_chat

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str = "demo-user"
    message: str

@router.post("")
async def chat(req: ChatRequest):
    """POST /chat — send a message and get an AI response."""
    reply = await handle_chat(req.user_id, req.message)
    return {"data": {"role": "assistant", "content": reply}}
