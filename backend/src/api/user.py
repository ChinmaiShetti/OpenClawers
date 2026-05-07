"""
src/api/user.py — User profile endpoints
"""
from fastapi import APIRouter

router = APIRouter()

# Hardcoded demo profile for Day 0 — replace with DB later
_DEMO_USER = {
    "user_id": "demo-user",
    "name": "Arjun",
    "email": "arjun@example.com",
    "phone": "+91XXXXXXXXXX",
    "preferences": {
        "nudge_enabled": True,
        "nudge_time": "08:00",
        "timezone": "Asia/Kolkata",
    },
}

@router.get("/profile")
def get_profile():
    """GET /user/profile"""
    return {"data": _DEMO_USER}

@router.put("/profile")
def update_profile(payload: dict):
    """PUT /user/profile — TODO: persist to DB"""
    _DEMO_USER.update(payload)
    return {"data": _DEMO_USER}
