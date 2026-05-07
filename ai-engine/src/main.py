"""
src/main.py — AI Engine entry point
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.priority_engine.router import router as priority_router
from src.reflection.router import router as reflection_router
from src.chat.router import router as chat_router
from src.meeting.router import router as meeting_router
from src.whatsapp.router import router as whatsapp_router

app = FastAPI(
    title="OpenClaw AI Engine",
    description="LLM orchestration, Priority Engine, Reflection Generator, MCP integrations",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["system"])
def health():
    return {"status": "ok", "service": "openclaw-ai-engine"}

app.include_router(chat_router,      prefix="/chat",      tags=["chat"])
app.include_router(priority_router,  prefix="/priority",  tags=["priority"])
app.include_router(reflection_router,prefix="/reflection", tags=["reflection"])
app.include_router(meeting_router,   prefix="/meeting",   tags=["meeting"])
app.include_router(whatsapp_router,  prefix="/whatsapp",  tags=["whatsapp"])
