"""
src/embeddings/pipeline.py
───────────────────────────
Nightly embedding pipeline:
  1. Pull today's logs from all 12 modules
  2. Chunk and embed using OpenAI text-embedding-3-small
  3. Upsert into Qdrant

Run manually: python -m src.embeddings.pipeline
Runs automatically via scheduler.py at midnight.
"""
import json
from datetime import datetime, date
from openai import OpenAI
from qdrant_client.models import PointStruct

from src.config import settings
from src.db.session import SessionLocal
from src.embeddings.client import ensure_collection, upsert_points

# Import all module models
from src.modules.financial.model import Transaction
from src.modules.sleep.model import SleepLog
from src.modules.fitness.model import WorkoutLog
from src.modules.books.model import BookEntry
from src.modules.academic.model import AcademicEntry

ALL_MODELS = [Transaction, SleepLog, WorkoutLog, BookEntry, AcademicEntry]
# TODO: add remaining 7 models once implemented

openai_client = OpenAI(api_key=settings.openai_api_key)


def embed_text(text: str) -> list[float]:
    response = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=text,
    )
    return response.data[0].embedding


def run_pipeline(target_date: date | None = None) -> int:
    """
    Embed all entries created on target_date (defaults to today).
    Returns the number of points upserted.
    """
    if target_date is None:
        target_date = date.today()

    ensure_collection(settings.qdrant_collection)
    db = SessionLocal()
    points_upserted = 0

    try:
        for Model in ALL_MODELS:
            entries = db.query(Model).filter(
                Model.created_at >= datetime.combine(target_date, datetime.min.time()),
                Model.created_at < datetime.combine(target_date, datetime.max.time()),
            ).all()

            for entry in entries:
                # Build a text representation of the entry for embedding
                text = f"Module: {Model.__tablename__}\n"
                for col in Model.__table__.columns:
                    val = getattr(entry, col.name, None)
                    if val is not None:
                        text += f"{col.name}: {val}\n"

                vector = embed_text(text)
                points_upserted += 1
                upsert_points(
                    settings.qdrant_collection,
                    [PointStruct(
                        id=entry.id,
                        vector=vector,
                        payload={
                            "module": Model.__tablename__,
                            "user_id": entry.user_id,
                            "created_at": str(entry.created_at),
                            "text": text,
                        },
                    )],
                )
    finally:
        db.close()

    print(f"[pipeline] Upserted {points_upserted} points for {target_date}")
    return points_upserted


if __name__ == "__main__":
    run_pipeline()
