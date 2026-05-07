"""
src/backend_client.py
──────────────────────
Thin HTTP client for calling the Backend API (port 8000).
AI Engine uses this to fetch module summaries, user profiles, etc.
"""
import httpx
from src.config import settings

_client = httpx.AsyncClient(base_url=settings.backend_url, timeout=30.0)


async def get_module_summary(module: str, user_id: str = "demo-user") -> dict:
    r = await _client.get(f"/modules/{module}/summary", params={"user_id": user_id})
    r.raise_for_status()
    return r.json()


async def get_all_summaries(user_id: str = "demo-user") -> list[dict]:
    modules = [
        "financial", "academic", "fitness", "sleep", "books",
        "good_deeds", "bad_deeds", "knowledge", "games", "concepts", "exams", "friends"
    ]
    summaries = []
    for module in modules:
        try:
            s = await get_module_summary(module, user_id)
            summaries.append(s)
        except Exception as e:
            summaries.append({"module": module, "error": str(e)})
    return summaries


async def get_user_profile(user_id: str = "demo-user") -> dict:
    r = await _client.get("/user/profile")
    r.raise_for_status()
    return r.json().get("data", {})
