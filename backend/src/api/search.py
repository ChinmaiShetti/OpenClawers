"""
src/api/search.py — Semantic search endpoint
Reads from Qdrant (written by the embedding pipeline).
"""
from fastapi import APIRouter, Query
from src.config import settings

router = APIRouter()

@router.get("")
async def search(q: str = Query(..., min_length=1)):
    """
    GET /search?q=...
    Performs semantic search across all module entries via Qdrant.

    TODO: Wire to embeddings/client.py once the embedding pipeline is running.
    Currently returns a stub response.
    """
    # STUB — replace with real Qdrant semantic search
    return {
        "data": [],
        "meta": {"query": q, "total": 0},
        "note": "Semantic search not yet wired — run the embedding pipeline first.",
    }
