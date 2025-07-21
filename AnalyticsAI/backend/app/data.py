import sqlalchemy
import requests
from app.config import settings

def get_engine():
    if settings.DB_TYPE == "duckdb":
        return sqlalchemy.create_engine(f"duckdb:///{settings.DB_PATH}")
    elif settings.DB_TYPE == "postgresql":
        return sqlalchemy.create_engine(
            f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
        )
    # Add more database types as needed
    raise ValueError("Unsupported DB type")

def query_sales_data(region: str = "Europe", quarter: str = "Q2") -> list:
    engine = get_engine()
    with engine.connect() as conn:
        # Example: create and populate table if not exists (for DuckDB demo)
        conn.execute(
            "CREATE TABLE IF NOT EXISTS sales (region VARCHAR, category VARCHAR, sales INT, quarter VARCHAR)"
        )
        conn.execute(
            "INSERT INTO sales VALUES ('Europe', 'Electronics', 120000, 'Q2'), ('Europe', 'Home Appliances', 90000, 'Q2'), ('Europe', 'Electronics', 135000, 'Q1'), ('Europe', 'Home Appliances', 83000, 'Q1')"
        )
        result = conn.execute(
            f"SELECT category, SUM(sales) as total_sales FROM sales WHERE region='{region}' AND quarter='{quarter}' GROUP BY category"
        )
        return [dict(row) for row in result]

def fetch_salesforce_data(query: str):
    # Real Salesforce REST API call (example, requires proper endpoint and auth)
    if not settings.SALESFORCE_API_KEY:
        return {"error": "No Salesforce API key configured"}
    url = f"https://your-instance.salesforce.com/services/data/vXX.X/query/?q={query}"
    headers = {"Authorization": f"Bearer {settings.SALESFORCE_API_KEY}"}
    resp = requests.get(url, headers=headers)
    return resp.json() if resp.status_code == 200 else {"error": resp.text}

def fetch_google_analytics_view(view_id: str, date_range: dict):
    # Example stub for Google Analytics Reporting API v4
    if not settings.GOOGLE_ANALYTICS_API_KEY:
        return {"error": "No Google Analytics API key configured"}
    # Implement real API call here
    return {"stub": "Implement Google Analytics API connection"}