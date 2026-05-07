"""src/reflection/generator.py"""
import json
from datetime import datetime
from src.backend_client import get_all_summaries
from src.llm.core import chat_completion
from src.llm.prompts import SYSTEM_REFLECTION

async def generate_reflection(period: str, user_id: str = "demo-user") -> dict:
    summaries = await get_all_summaries(user_id)
    prompt = f"Period: {period}\nModule data:\n{json.dumps(summaries, indent=2)}"
    raw = await chat_completion(
        messages=[{"role": "user", "content": prompt}],
        system=SYSTEM_REFLECTION,
        max_tokens=2048,
    )
    try:
        result = json.loads(raw)
    except json.JSONDecodeError:
        result = {"narrative": raw, "highlights": [], "concerns": []}
    result["period"] = period
    result["generated_at"] = datetime.utcnow().isoformat()
    return result
