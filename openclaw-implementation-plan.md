# OpenClaw — Implementation Plan & Team Distribution

> Samsung Hackathon · Theme: Daily Utility and More

---

## What We're Building

OpenClaw is a unified self-analysis platform that consolidates 12 life modules (finance, fitness, academics, sleep, books, etc.) under a single AI-powered interface. The AI remembers everything via a Vector DB, acts on the world through MCP integrations (Notion, Slack, GitHub, Google Calendar), and reaches the user proactively through WhatsApp nudges.

---

## Team Split — 3 People, Clean Boundaries

| Person | Domain | What They Own |
|--------|--------|---------------|
| **P1** | Frontend | All UI — dashboard, module entry forms, AI chat panel, Samsung-optimised responsive design |
| **P2** | Backend + Data | REST API, all 12 module schemas + CRUD, SQLite/Postgres DB, nightly embedding pipeline, Vector DB writes |
| **P3** | AI Engine + Integrations | LLM orchestration, Priority Engine, Reflection Generator, MCP integrations, WhatsApp nudge system |

The critical rule: **each person's directory is their kingdom**. Nobody edits another's folder. Integration happens only through well-defined API contracts declared in `/shared`.

---

## Monorepo Folder Structure

```
openclaw/
│
├── README.md
├── docker-compose.yml          ← stitches all three services together
├── .env.example                ← all env vars documented here
│
├── shared/                     ← NOBODY EDITS THIS ALONE — agree together
│   ├── types/
│   │   ├── modules.ts          ← type definitions for all 12 modules
│   │   ├── api.ts              ← request/response shapes for every endpoint
│   │   └── user.ts             ← user and session types
│   └── constants/
│       └── index.ts            ← module names, threshold values, etc.
│
├── frontend/                   ← PERSON 1
├── backend/                    ← PERSON 2
└── ai-engine/                  ← PERSON 3
```

---

## Frontend — Person 1

**Stack:** Next.js 14 (App Router) + Tailwind CSS + shadcn/ui  
**Port:** 3000  
**Talks to:** Backend REST API at `localhost:8000`

```
frontend/
├── package.json
├── next.config.ts
├── tailwind.config.ts
├── .env.local.example          ← NEXT_PUBLIC_API_URL=http://localhost:8000
│
└── src/
    ├── app/
    │   ├── layout.tsx
    │   ├── page.tsx              ← redirects to /dashboard
    │   ├── dashboard/
    │   │   └── page.tsx          ← main dashboard (priority list + module tiles)
    │   ├── modules/
    │   │   ├── financial/page.tsx
    │   │   ├── academic/page.tsx
    │   │   ├── fitness/page.tsx
    │   │   ├── sleep/page.tsx
    │   │   ├── books/page.tsx
    │   │   ├── good-deeds/page.tsx
    │   │   ├── bad-deeds/page.tsx
    │   │   ├── knowledge/page.tsx
    │   │   ├── games/page.tsx
    │   │   ├── concepts/page.tsx
    │   │   ├── exams/page.tsx
    │   │   └── friends/page.tsx
    │   ├── chat/
    │   │   └── page.tsx          ← AI conversation panel
    │   └── reflection/
    │       └── page.tsx          ← weekly/monthly reflection viewer
    │
    ├── components/
    │   ├── dashboard/
    │   │   ├── PriorityList.tsx  ← ranked daily focus items
    │   │   ├── ModuleTiles.tsx   ← 12 module quick-access tiles
    │   │   └── DailySnapshot.tsx ← today's summary card
    │   │
    │   ├── modules/
    │   │   ├── financial/
    │   │   │   ├── TransactionForm.tsx
    │   │   │   └── FinancialSummary.tsx
    │   │   ├── academic/
    │   │   │   ├── CourseCard.tsx
    │   │   │   └── GradeEntry.tsx
    │   │   ├── fitness/
    │   │   │   ├── WorkoutLogger.tsx
    │   │   │   └── MacroTracker.tsx
    │   │   ├── sleep/
    │   │   │   └── SleepLogger.tsx
    │   │   ├── books/
    │   │   │   └── BookCard.tsx
    │   │   └── shared/
    │   │       ├── LogEntryCard.tsx   ← reusable log entry wrapper
    │   │       └── TrendChart.tsx     ← reusable sparkline/trend
    │   │
    │   ├── chat/
    │   │   ├── ChatWindow.tsx
    │   │   ├── MessageBubble.tsx
    │   │   └── InputBar.tsx
    │   │
    │   └── ui/                   ← shadcn components live here (auto-generated)
    │
    ├── hooks/
    │   ├── useModuleData.ts      ← generic hook: fetch + mutate any module
    │   ├── usePriority.ts        ← fetch priority list from backend
    │   └── useChat.ts            ← streaming chat hook
    │
    └── lib/
        └── api.ts                ← typed fetch wrapper (uses shared/types/api.ts)
```

**Person 1's Day 1 tasks:**
1. Scaffold Next.js project, set up Tailwind + shadcn
2. Build the Dashboard page with hardcoded mock data
3. Build one complete module page (Financial) end to end
4. Wire `lib/api.ts` to the backend once P2 has endpoints up

---

## Backend — Person 2

**Stack:** Python + FastAPI + SQLite (dev) → Postgres (prod) + SQLAlchemy + Qdrant (vector DB)  
**Port:** 8000  
**Talks to:** Qdrant at `localhost:6333`, AI engine at `localhost:9000`

```
backend/
├── requirements.txt
├── .env.example               ← DATABASE_URL, QDRANT_URL, OPENAI_API_KEY (for embeddings)
├── Dockerfile
│
└── src/
    ├── main.py                ← FastAPI app init, router registration, CORS
    ├── config.py              ← env var loading
    ├── dependencies.py        ← DB session, auth dependency
    │
    ├── db/
    │   ├── base.py            ← SQLAlchemy declarative base
    │   ├── session.py         ← engine + session factory
    │   └── migrations/        ← Alembic migration files
    │
    ├── modules/               ← one sub-package per life module
    │   ├── _base/
    │   │   ├── model.py       ← abstract base ORM model (id, user_id, created_at)
    │   │   ├── schema.py      ← abstract Pydantic base
    │   │   └── router.py      ← abstract CRUD router factory
    │   │
    │   ├── financial/
    │   │   ├── model.py       ← Transaction ORM model
    │   │   ├── schema.py      ← TransactionCreate, TransactionRead, FinancialSummary
    │   │   └── router.py      ← GET /financial, POST /financial, GET /financial/summary
    │   │
    │   ├── academic/
    │   │   ├── model.py       ← Course, Assignment, Grade models
    │   │   ├── schema.py
    │   │   └── router.py      ← GET /academic/courses, POST /academic/grade, etc.
    │   │
    │   ├── fitness/
    │   │   ├── model.py       ← Workout, FoodEntry, BodyMetric
    │   │   ├── schema.py
    │   │   └── router.py
    │   │
    │   ├── sleep/
    │   │   ├── model.py
    │   │   ├── schema.py
    │   │   └── router.py
    │   │
    │   ├── books/
    │   │   ├── model.py
    │   │   ├── schema.py
    │   │   └── router.py
    │   │
    │   ├── good_deeds/        ← same structure for remaining 7 modules
    │   ├── bad_deeds/
    │   ├── knowledge/
    │   ├── games/
    │   ├── concepts/
    │   ├── exams/
    │   └── friends/
    │
    ├── embeddings/
    │   ├── pipeline.py        ← nightly job: pull today's logs → chunk → embed → upsert to Qdrant
    │   ├── scheduler.py       ← APScheduler setup (runs pipeline at midnight)
    │   └── client.py          ← Qdrant client wrapper (upsert, search)
    │
    └── api/
        ├── user.py            ← GET /user/profile, PUT /user/profile
        └── search.py          ← GET /search?q=... → semantic search via Qdrant
```

**Person 2's API contract to expose (P1 and P3 depend on these):**

```
GET  /modules/{module}/entries?limit=20&offset=0
POST /modules/{module}/entries
GET  /modules/{module}/summary          ← aggregated stats (used by dashboard + AI)
GET  /priority                          ← current ranked focus list
GET  /search?q={query}                  ← semantic search across all modules
GET  /user/profile
PUT  /user/profile
```

**Person 2's Day 1 tasks:**
1. Set up FastAPI + SQLAlchemy + Alembic
2. Build the `_base` router factory so adding new modules is 10 lines
3. Build Financial + Sleep modules fully
4. Start Qdrant + document the embedding schema

---

## AI Engine — Person 3

**Stack:** Python + FastAPI (or plain Flask) + LangChain/direct Anthropic SDK + MCP clients  
**Port:** 9000  
**Talks to:** Backend API at `localhost:8000`, external APIs (Notion, Slack, GitHub, GCal, WhatsApp)

```
ai-engine/
├── requirements.txt
├── .env.example               ← ANTHROPIC_API_KEY, NOTION_TOKEN, SLACK_TOKEN,
│                              ←   GITHUB_TOKEN, GOOGLE_CREDENTIALS_JSON, WHATSAPP_API_KEY
├── Dockerfile
│
└── src/
    ├── main.py                ← FastAPI app, route registration
    ├── config.py
    ├── backend_client.py      ← thin HTTP client to call backend:8000
    │
    ├── llm/
    │   ├── core.py            ← Anthropic client setup, base chat function
    │   ├── prompts.py         ← all system prompts (priority, reflection, nudge, chat)
    │   └── conversation.py    ← multi-turn chat state management
    │
    ├── priority_engine/
    │   ├── engine.py          ← pulls module summaries → ranks by urgency + impact
    │   ├── rules.py           ← threshold rules (sleep < 6h for 3 days → high priority)
    │   └── router.py          ← POST /priority/compute → returns ranked list
    │
    ├── reflection/
    │   ├── generator.py       ← daily/weekly/monthly/annual narrative generation
    │   ├── scheduler.py       ← triggers reflection at configured intervals
    │   └── router.py          ← POST /reflection/generate?period=daily
    │
    ├── vector_db/
    │   ├── search.py          ← semantic query against Qdrant (P3 reads, P2 writes)
    │   └── context.py         ← assembles relevant past chapters for LLM context
    │
    ├── mcp/
    │   ├── base.py            ← MCP client base class (structured function call dispatcher)
    │   ├── notion/
    │   │   ├── client.py      ← Notion API wrapper
    │   │   └── tools.py       ← MCP tool definitions: create_page, update_database, etc.
    │   ├── slack/
    │   │   ├── client.py
    │   │   └── tools.py       ← send_message, post_to_channel
    │   ├── github/
    │   │   ├── client.py
    │   │   └── tools.py       ← list_commits, get_pr_status
    │   ├── calendar/
    │   │   ├── client.py      ← Google Calendar API
    │   │   └── tools.py       ← get_events, create_reminder, cancel_event
    │   └── dispatcher.py      ← routes LLM tool_use responses to the right MCP client
    │
    ├── whatsapp/
    │   ├── sender.py          ← WhatsApp Business API wrapper (send message)
    │   ├── templates.py       ← nudge message templates by alert type
    │   └── router.py          ← POST /whatsapp/nudge (called by scheduler)
    │
    ├── meeting/
    │   ├── pre_fill.py        ← auto-generates note template from calendar event
    │   ├── processor.py       ← extracts action items from meeting notes
    │   └── router.py          ← POST /meeting/prepare, POST /meeting/process
    │
    └── chat/
        ├── handler.py         ← main chat endpoint: user query → context assembly → LLM → response
        └── router.py          ← POST /chat (streaming)
```

**Person 3's API contract to expose (P1 depends on these):**

```
POST /chat                              ← streaming chat with full context
POST /priority/compute                  ← compute and return ranked priority list
POST /reflection/generate?period=daily  ← generate narrative reflection
POST /meeting/prepare                   ← pre-fill meeting notes from calendar
POST /meeting/process                   ← extract action items from meeting notes
POST /whatsapp/nudge                    ← manual nudge trigger (for demo)
```

**Person 3's Day 1 tasks:**
1. Set up Anthropic SDK, test basic chat flow
2. Build Priority Engine logic (rule-based first, LLM-enhanced second)
3. Wire one MCP integration (Google Calendar) end to end
4. Build the `/chat` endpoint with Qdrant context injection

---

## Shared Types — Define on Day 0

Everyone agrees on these before writing a single line of feature code:

```typescript
// shared/types/modules.ts

export type ModuleName =
  | 'financial' | 'good_deeds' | 'bad_deeds' | 'academic'
  | 'exams' | 'fitness' | 'knowledge' | 'sleep'
  | 'games' | 'concepts' | 'books' | 'friends'

export interface ModuleEntry {
  id: string
  module: ModuleName
  user_id: string
  data: Record<string, unknown>   // module-specific payload
  created_at: string
}

export interface PriorityItem {
  module: ModuleName
  title: string
  description: string
  urgency: 'high' | 'medium' | 'low'
  impact: 'high' | 'medium' | 'low'
  score: number                   // 0–100 composite
}

export interface ReflectionResult {
  period: 'daily' | 'weekly' | 'monthly' | 'annual'
  narrative: string
  highlights: string[]
  concerns: string[]
  generated_at: string
}
```

```typescript
// shared/types/api.ts

export interface ApiResponse<T> {
  data: T
  error?: string
}

export interface ChatMessage {
  role: 'user' | 'assistant'
  content: string
}

export interface ChatRequest {
  messages: ChatMessage[]
  user_id: string
}
```

---

## Docker Compose — Merge Point

This is how everything snaps together. P2 writes this:

```yaml
# docker-compose.yml
version: '3.9'

services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://backend:8000
      - NEXT_PUBLIC_AI_URL=http://ai-engine:9000
    depends_on:
      - backend
      - ai-engine

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=sqlite:///./openclaw.db
      - QDRANT_URL=http://qdrant:6333
    depends_on:
      - qdrant

  ai-engine:
    build: ./ai-engine
    ports:
      - "9000:9000"
    environment:
      - BACKEND_URL=http://backend:8000
      - QDRANT_URL=http://qdrant:6333
    depends_on:
      - backend
      - qdrant

  qdrant:
    image: qdrant/qdrant
    ports:
      - "6333:6333"
    volumes:
      - qdrant_data:/qdrant/storage

volumes:
  qdrant_data:
```

---

## Hackathon Phase Mapping

| Phase (from doc) | Who | Target |
|-----------------|-----|--------|
| Phase 1 — Core Logging | P1 + P2 | Module forms live, data persists to SQLite |
| Phase 2 — AI Integration | P3 | `/chat` endpoint live, Priority Engine running |
| Phase 3 — Vector Memory | P2 + P3 | Embedding pipeline nightly, semantic search working |
| Phase 4 — Integrations | P3 | GCal + Notion MCP wired, at least 2 integrations demo-ready |
| Phase 5 — WhatsApp Nudges | P3 | Nudge templates live, triggered by threshold breach |
| Phase 6 — Demo & Polish | All | Arjun's sample journey end-to-end, Samsung UI optimisation |

---

## Day 0 Checklist (Everyone Together)

- [ ] Create the monorepo on GitHub, add all three as collaborators
- [ ] Agree on and commit `shared/types/modules.ts` and `shared/types/api.ts`
- [ ] Each person creates their folder, adds `README.md` with their API contracts
- [ ] Set up a branch strategy: `main` (protected), `p1/feature-x`, `p2/feature-x`, `p3/feature-x`
- [ ] Commit the `docker-compose.yml` and `.env.example` to `main`
- [ ] Everyone can run `docker-compose up` by end of Day 0

---

## Merge Strategy

Each person works on their own branch and merges into `main` only when:

1. Their service starts without errors (`docker-compose up` still works)
2. Their API endpoints return valid responses (even mocked)
3. There are no changes to another person's folder

Final integration PR happens in Phase 6 — one person (P2 recommended) drives the `docker-compose` merge, others review their own service logs.

---

## Demo Script — Arjun's Journey

Mapped to actual feature calls:

| Moment | Feature | Service |
|--------|---------|---------|
| Morning WhatsApp: "You slept 5.2h…" | WhatsApp nudge triggered by sleep threshold | AI Engine → WhatsApp |
| Arjun logs freelancing payment | Financial module POST | Backend → Frontend |
| OpenClaw flags savings 12% below target | Priority Engine recomputes | AI Engine |
| Evening: logs book chapter | Books module POST + Concept Log link | Backend |
| Night: daily reflection generated | Reflection generator | AI Engine |
| Weekly: pushed to Notion journal | Notion MCP tool call | AI Engine → Notion |

---

*OpenClaw — Know Yourself. Master Your Day. Own Your Future.*
