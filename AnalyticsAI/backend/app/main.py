from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.agent import agentic_workflow

app = FastAPI(
    title="AnalyticsAI Agentic Platform",
    description="Enterprise AI-powered analytics with agentic workflows",
    version="2.0.0"
)

@app.get("/api/status")
async def health():
    return {"status": "ok"}

@app.post("/api/agent")
async def agent_endpoint(request: Request):
    body = await request.json()
    query = body.get("query", "")
    result = agentic_workflow(query)
    return JSONResponse(result)