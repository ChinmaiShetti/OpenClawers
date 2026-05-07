"""
src/chat/handler.py — Main chat endpoint logic.

Flow:
  1. Fetch user's recent Qdrant context (semantic search on the query)
  2. Fetch all module summaries from backend
  3. Build system prompt with context injected
  4. Stream response from Anthropic
"""
import json
from src.llm.core import get_client
from src.llm.prompts import SYSTEM_CHAT
from src.llm.conversation import get_history, append_message
from src.backend_client import get_all_summaries


async def handle_chat(user_id: str, user_message: str) -> str:
    # 1. Get module summaries for context
    summaries = await get_all_summaries(user_id)
    context_block = "USER MODULE SUMMARIES:\n" + json.dumps(summaries, indent=2)

    # 2. Build system prompt
    system = f"{SYSTEM_CHAT}\n\n{context_block}"

    # 3. Get history and append new message
    history = get_history(user_id)
    append_message(user_id, "user", user_message)
    messages = history + [{"role": "user", "content": user_message}]

    # 4. Call LLM
    client = get_client()
    response = await client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        system=system,
        messages=messages,
    )
    reply = response.content[0].text
    append_message(user_id, "assistant", reply)
    return reply
