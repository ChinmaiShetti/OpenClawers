"""
src/priority_engine/engine.py
──────────────────────────────
Pulls module summaries → applies threshold rules → asks LLM to rank.
"""
import json
from src.backend_client import get_all_summaries
from src.llm.core import chat_completion
from src.llm.prompts import SYSTEM_PRIORITY
from src.priority_engine.rules import apply_rules


async def compute_priority(user_id: str = "demo-user") -> list[dict]:
    summaries = await get_all_summaries(user_id)

    # Apply deterministic rules first
    rule_flags = apply_rules(summaries)

    prompt = f"""Module Summaries:
{json.dumps(summaries, indent=2)}

Rule-based flags (these MUST appear as high urgency):
{json.dumps(rule_flags, indent=2)}

Rank all relevant modules and return the JSON priority list."""

    raw = await chat_completion(
        messages=[{"role": "user", "content": prompt}],
        system=SYSTEM_PRIORITY,
        max_tokens=1024,
    )

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Fallback: return rule-based flags only
        return rule_flags
