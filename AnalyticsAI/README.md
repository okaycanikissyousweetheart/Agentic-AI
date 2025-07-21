# AnalyticsAI (Agentic Dashboard Platform)

A next-gen analytics platform powered by agentic AI.  
Ask questions, get actionable dashboards, insights, and recommendations—fused from all your business data.

## Features

- Natural language analytics (ask for anything)
- Dynamic, interactive dashboards generated on demand
- Multi-source data integration (Sales, CRM, Marketing, etc.)
- AI-powered insights & action recommendations
- Real business data connectors (SQL, Salesforce, Google Analytics)
- Agentic workflow: task decomposition, tool use, error handling

## Quick Start

### Backend
```bash
cd analyticsai/backend
python3 -m venv env && source env/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Add your OpenAI API key to .env
uvicorn app.main:app --reload
```

### Frontend
```bash
cd analyticsai/frontend
npm install
npm start
```

### Docs
See [docs/agentic-ai-example.md](docs/agentic-ai-example.md) for agentic AI background.

---

*Submodule of @okaycanikissyousweetheart/Agentic-AI*