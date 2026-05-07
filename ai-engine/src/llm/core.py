"""
src/llm/core.py — Anthropic client setup
"""
import anthropic
from src.config import settings

_client: anthropic.AsyncAnthropic | None = None

def get_client() -> anthropic.AsyncAnthropic:
    global _client
    if _client is None:
        _client = anthropic.AsyncAnthropic(api_key=settings.anthropic_api_key)
    return _client

async def chat_completion(
    messages: list[dict],
    system: str = "",
    model: str = "claude-3-5-sonnet-20241022",
    max_tokens: int = 2048,
) -> str:
    """Simple (non-streaming) chat completion."""
    client = get_client()
    response = await client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        messages=messages,
    )
    return response.content[0].text
