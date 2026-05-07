# OpenClaw 🦞

> Samsung Hackathon · Theme: Daily Utility and More

**Know Yourself. Master Your Day. Own Your Future.**

OpenClaw is a unified self-analysis platform that consolidates **12 life modules** (finance, fitness, academics, sleep, books, and more) under a single AI-powered interface. The AI remembers everything via a Vector DB, acts on the world through MCP integrations (Notion, Slack, GitHub, Google Calendar), and reaches the user proactively through WhatsApp nudges.

---

## Architecture

```
openclaw/
├── frontend/       → Next.js 14 (Port 3000)   — Person 1
├── backend/        → FastAPI    (Port 8000)   — Person 2
├── ai-engine/      → FastAPI    (Port 9000)   — Person 3
└── shared/         → TypeScript types (no one owns this alone)
```

## Quick Start (Docker)

```bash
cp .env.example .env        # fill in your secrets
docker-compose up --build
```

| Service    | URL                    |
|------------|------------------------|
| Frontend   | http://localhost:3000  |
| Backend    | http://localhost:8000  |
| AI Engine  | http://localhost:9000  |
| Qdrant UI  | http://localhost:6333  |

## Quick Start (Local Dev — no Docker)

```bash
# Terminal 1 — Backend
cd backend
pip install -r requirements.txt
cp .env.example .env
uvicorn src.main:app --reload --port 8000

# Terminal 2 — AI Engine
cd ai-engine
pip install -r requirements.txt
cp .env.example .env
uvicorn src.main:app --reload --port 9000

# Terminal 3 — Frontend
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

## Branch Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Protected — only merged PRs |
| `p1/feature-name` | Person 1 (Frontend) work |
| `p2/feature-name` | Person 2 (Backend) work |
| `p3/feature-name` | Person 3 (AI Engine) work |

**Golden rule:** Never edit another person's folder. Integration only through REST APIs defined in each service's README.

## The 12 Life Modules

| # | Module | Description |
|---|--------|-------------|
| 1 | Financial | Income, expenses, savings tracking |
| 2 | Academic | Courses, grades, assignments |
| 3 | Fitness | Workouts, macros, body metrics |
| 4 | Sleep | Sleep duration, quality logs |
| 5 | Books | Reading log, notes |
| 6 | Good Deeds | Positive actions tracker |
| 7 | Bad Deeds | Habit awareness tracker |
| 8 | Knowledge | Things learned daily |
| 9 | Games | Gaming sessions & reflection |
| 10 | Concepts | Ideas and mental models |
| 11 | Exams | Upcoming exams, scores |
| 12 | Friends | Relationships & social log |

---

*OpenClaw — Know Yourself. Master Your Day. Own Your Future.*
