from fastapi import APIRouter
from pydantic import BaseModel
from src.llm.core import chat_completion
from src.llm.prompts import SYSTEM_MEETING_PREP, SYSTEM_MEETING_PROCESS

router = APIRouter()

class MeetingPrepRequest(BaseModel):
    calendar_event_id: str
    user_id: str = "demo-user"

class MeetingProcessRequest(BaseModel):
    notes: str
    user_id: str = "demo-user"

@router.post("/prepare")
async def prepare(req: MeetingPrepRequest):
    """POST /meeting/prepare — generates a note template."""
    # TODO: fetch actual calendar event via Google Calendar MCP
    prompt = f"Prepare meeting notes for calendar event: {req.calendar_event_id}"
    result = await chat_completion(
        messages=[{"role": "user", "content": prompt}],
        system=SYSTEM_MEETING_PREP,
    )
    return {"data": {"template": result}}

@router.post("/process")
async def process(req: MeetingProcessRequest):
    """POST /meeting/process — extracts action items from notes."""
    import json
    raw = await chat_completion(
        messages=[{"role": "user", "content": req.notes}],
        system=SYSTEM_MEETING_PROCESS,
    )
    try:
        return {"data": json.loads(raw)}
    except json.JSONDecodeError:
        return {"data": {"action_items": [], "summary": raw}}
