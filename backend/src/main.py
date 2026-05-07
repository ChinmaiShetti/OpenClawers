# src/main.py — Backend entry point
# ─────────────────────────────────────────────────────────────
# FastAPI app init, CORS, health check, and router registration.
# ─────────────────────────────────────────────────────────────

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.db.session import engine
from src.db.base import Base

# ── Module routers ────────────────────────────────────────────
from src.modules.financial.router import router as financial_router
from src.modules.academic.router import router as academic_router
from src.modules.fitness.router import router as fitness_router
from src.modules.sleep.router import router as sleep_router
from src.modules.books.router import router as books_router
from src.modules.good_deeds.router import router as good_deeds_router
from src.modules.bad_deeds.router import router as bad_deeds_router
from src.modules.knowledge.router import router as knowledge_router
from src.modules.games.router import router as games_router
from src.modules.concepts.router import router as concepts_router
from src.modules.exams.router import router as exams_router
from src.modules.friends.router import router as friends_router

# ── API routers ───────────────────────────────────────────────
from src.api.user import router as user_router
from src.api.search import router as search_router

# ── Create DB tables on startup ───────────────────────────────
Base.metadata.create_all(bind=engine)

# ── App ───────────────────────────────────────────────────────
app = FastAPI(
    title="OpenClaw Backend",
    description="REST API for all 12 life modules + embeddings + search",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS (allow frontend + ai-engine) ────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:9000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Health check ──────────────────────────────────────────────
@app.get("/health", tags=["system"])
def health():
    return {"status": "ok", "service": "openclaw-backend"}

# ── Register all routers ──────────────────────────────────────
# Module routers — each mounts at /modules/{module}/...
app.include_router(financial_router,  prefix="/modules/financial",  tags=["financial"])
app.include_router(academic_router,   prefix="/modules/academic",   tags=["academic"])
app.include_router(fitness_router,    prefix="/modules/fitness",    tags=["fitness"])
app.include_router(sleep_router,      prefix="/modules/sleep",      tags=["sleep"])
app.include_router(books_router,      prefix="/modules/books",      tags=["books"])
app.include_router(good_deeds_router, prefix="/modules/good_deeds", tags=["good_deeds"])
app.include_router(bad_deeds_router,  prefix="/modules/bad_deeds",  tags=["bad_deeds"])
app.include_router(knowledge_router,  prefix="/modules/knowledge",  tags=["knowledge"])
app.include_router(games_router,      prefix="/modules/games",      tags=["games"])
app.include_router(concepts_router,   prefix="/modules/concepts",   tags=["concepts"])
app.include_router(exams_router,      prefix="/modules/exams",      tags=["exams"])
app.include_router(friends_router,    prefix="/modules/friends",    tags=["friends"])

# API routers
app.include_router(user_router,   prefix="/user",   tags=["user"])
app.include_router(search_router, prefix="/search", tags=["search"])
