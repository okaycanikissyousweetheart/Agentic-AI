from app.config import settings
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool

def get_llm():
    if settings.LLM_PROVIDER == "openai":
        return OpenAI(openai_api_key=settings.OPENAI_API_KEY)
    # Add other providers here
    raise ValueError("Unsupported LLM provider")

def sales_query_tool(query: str) -> str:
    # Placeholder for actual sales DB/API query logic
    return f"Queried sales for: {query}"

tools = [
    Tool(
        name="sales_query",
        func=sales_query_tool,
        description="Fetches sales data given a natural language query"
    ),
    # Add more tools here
]

def analytics_agent(user_query: str):
    llm = get_llm()
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    response = agent.run(user_query)
    return response