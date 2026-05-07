"""
src/llm/conversation.py — Multi-turn chat state management.
Keeps the last N messages in memory. Extend with Redis/DB for persistence.
"""
from collections import deque

MAX_HISTORY = 20

# In-memory store keyed by user_id
_histories: dict[str, deque] = {}


def get_history(user_id: str) -> list[dict]:
    return list(_histories.get(user_id, deque()))


def append_message(user_id: str, role: str, content: str) -> None:
    if user_id not in _histories:
        _histories[user_id] = deque(maxlen=MAX_HISTORY)
    _histories[user_id].append({"role": role, "content": content})


def clear_history(user_id: str) -> None:
    _histories.pop(user_id, None)
