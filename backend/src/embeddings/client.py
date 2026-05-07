"""
src/embeddings/client.py
─────────────────────────
Qdrant client wrapper — upsert and search operations.
"""
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from src.config import settings

_client: QdrantClient | None = None


def get_qdrant() -> QdrantClient:
    global _client
    if _client is None:
        _client = QdrantClient(url=settings.qdrant_url)
    return _client


def ensure_collection(collection: str, vector_size: int = 1536) -> None:
    """Create collection if it doesn't exist."""
    client = get_qdrant()
    existing = [c.name for c in client.get_collections().collections]
    if collection not in existing:
        client.create_collection(
            collection_name=collection,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )


def upsert_points(collection: str, points: list[PointStruct]) -> None:
    client = get_qdrant()
    client.upsert(collection_name=collection, points=points)


def search_points(collection: str, vector: list[float], top_k: int = 5) -> list[dict]:
    client = get_qdrant()
    results = client.search(collection_name=collection, query_vector=vector, limit=top_k)
    return [{"id": r.id, "score": r.score, "payload": r.payload} for r in results]
