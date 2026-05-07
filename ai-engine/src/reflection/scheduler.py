"""src/reflection/scheduler.py — Triggers reflection generation at configured intervals."""
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def start_scheduler():
    # TODO: wire to generate_reflection() calls
    scheduler.start()
    print("[reflection scheduler] started.")

def stop_scheduler():
    scheduler.shutdown()
