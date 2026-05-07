# AI Engine — Person 3

**Stack:** Python 3.11 · FastAPI · Anthropic Claude · Qdrant · MCP clients  
**Port:** 9000

## Run Locally

```bash
cd ai-engine
pip install -r requirements.txt
cp .env.example .env    # fill in ANTHROPIC_API_KEY etc.
uvicorn src.main:app --reload --port 9000
```

## API Contract (what P1 depends on)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| POST | `/chat` | Streaming chat with full context |
| POST | `/priority/compute` | Compute and return ranked priority list |
| POST | `/reflection/generate?period=daily` | Generate narrative reflection |
| POST | `/meeting/prepare` | Pre-fill meeting notes from calendar |
| POST | `/meeting/process` | Extract action items from notes |
| POST | `/whatsapp/nudge` | Manual nudge trigger (for demo) |

## Folder Structure

```
src/
├── main.py              ← FastAPI app, router registration, CORS
├── config.py
├── backend_client.py    ← HTTP client to call backend:8000
├── llm/                 ← Anthropic setup, prompts, conversation state
├── priority_engine/     ← module summary → urgency ranking
├── reflection/          ← daily/weekly/monthly narrative generation
├── vector_db/           ← Qdrant reads for context injection
├── mcp/                 ← Notion, Slack, GitHub, Calendar tool dispatching
├── whatsapp/            ← nudge sending via WhatsApp Business API
├── meeting/             ← meeting prep + action item extraction
└── chat/                ← main streaming chat handler
```
