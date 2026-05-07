# Backend — Person 2

**Stack:** Python 3.11 · FastAPI · SQLAlchemy 2 · SQLite (dev) · Qdrant  
**Port:** 8000

## Run Locally

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
uvicorn src.main:app --reload --port 8000
```

## API Contract (what P1 and P3 depend on)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| GET | `/modules/{module}/entries?limit=20&offset=0` | List entries for a module |
| POST | `/modules/{module}/entries` | Create a new entry |
| GET | `/modules/{module}/summary` | Aggregated stats |
| GET | `/priority` | Current ranked focus list |
| GET | `/search?q={query}` | Semantic search across all modules |
| GET | `/user/profile` | Get user profile |
| PUT | `/user/profile` | Update user profile |

## Folder Structure

```
src/
├── main.py          ← FastAPI app, router registration, CORS
├── config.py        ← env var loading (Pydantic Settings)
├── dependencies.py  ← DB session, auth dependencies
├── db/
│   ├── base.py      ← SQLAlchemy declarative base
│   └── session.py   ← engine + session factory
├── modules/
│   ├── _base/       ← abstract model/schema/router factory
│   ├── financial/
│   ├── academic/
│   ├── fitness/
│   ├── sleep/
│   ├── books/
│   └── ...          ← 7 more modules
├── embeddings/      ← nightly pipeline → Qdrant
└── api/
    ├── user.py
    └── search.py
```

## Adding a New Module

1. Copy `src/modules/sleep/` as a template
2. Edit `model.py` (ORM), `schema.py` (Pydantic), `router.py` (endpoints)
3. Register the router in `src/main.py` (one line)

Done. The `_base` router factory handles all the CRUD boilerplate.
