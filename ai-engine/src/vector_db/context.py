"""src/vector_db/context.py — Assembles relevant past data for LLM context."""
from src.vector_db.search import search

async def assemble_context(query_vector: list[float]) -> str:
    results = await search(query_vector, top_k=5)
    if not results:
        return ""
    return "\n".join(r.get("payload", {}).get("text", "") for r in results)
