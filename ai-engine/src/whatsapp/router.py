from fastapi import APIRouter
from pydantic import BaseModel
from src.llm.core import chat_completion
from src.llm.prompts import SYSTEM_NUDGE

router = APIRouter()

class NudgeRequest(BaseModel):
    alert_type: str          # e.g. "sleep_deficit", "savings_gap"
    context: str             # e.g. "average sleep 5.2h for 3 days"
    user_id: str = "demo-user"

@router.post("/nudge")
async def nudge(req: NudgeRequest):
    """POST /whatsapp/nudge — generate and (stub) send a WhatsApp nudge."""
    prompt = f"Alert: {req.alert_type}\nContext: {req.context}"
    message = await chat_completion(
        messages=[{"role": "user", "content": prompt}],
        system=SYSTEM_NUDGE,
        max_tokens=200,
    )
    # TODO: wire to WhatsApp Business API sender
    return {
        "data": {
            "message": message,
            "status": "generated (not sent — wire WHATSAPP_API_KEY to enable)",
        }
    }
