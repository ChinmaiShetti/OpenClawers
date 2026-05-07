"""
src/embeddings/scheduler.py
─────────────────────────────
APScheduler setup — runs the embedding pipeline nightly at midnight.
Called from main.py startup events (TODO: wire to lifespan).
"""
from apscheduler.schedulers.background import BackgroundScheduler
from src.embeddings.pipeline import run_pipeline

scheduler = BackgroundScheduler()


def start_scheduler():
    scheduler.add_job(run_pipeline, "cron", hour=0, minute=0, id="nightly_embed")
    scheduler.start()
    print("[scheduler] Embedding pipeline scheduled at midnight.")


def stop_scheduler():
    scheduler.shutdown()
