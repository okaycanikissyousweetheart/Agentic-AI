import openai
from app.config import settings
from app.data import query_sales_data, fetch_salesforce_data, fetch_google_analytics_view

openai.api_key = settings.OPENAI_API_KEY

def extract_query_params(query: str) -> dict:
    # Simple NLP stub (use LLM or regex for real use)
    region = "Europe" if "Europe" in query else "Global"
    quarter = "Q2" if "last quarter" in query else "Q1"
    return {"region": region, "quarter": quarter}

def agentic_workflow(user_query: str):
    params = extract_query_params(user_query)
    # Step 1: Pull sales data from DB
    sales_data = query_sales_data(params["region"], params["quarter"])
    # Step 2: Optionally query external sources (Salesforce, Google Analytics)
    # salesforce_data = fetch_salesforce_data("SELECT ...")  # Example
    # ga_data = fetch_google_analytics_view("view_id", {"start": "2024-04-01", "end": "2024-06-30"})
    # Step 3: Compose prompt for LLM
    prompt = f"""
    User question: '{user_query}'
    Sales data by category: {sales_data}
    - Summarize sales performance
    - Highlight areas needing improvement
    - Compare with previous period if relevant
    - Suggest next actions
    """
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an analytics expert for business intelligence."},
            {"role": "user", "content": prompt}
        ]
    )
    summary = resp.choices[0].message.content
    return {
        "summary": summary,
        "sales_data": sales_data,
        # "salesforce_data": salesforce_data,
        # "google_analytics_data": ga_data
    }