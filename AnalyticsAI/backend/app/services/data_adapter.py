import os
import sqlalchemy

from app.config import settings

class DataAdapter:
    def __init__(self):
        db_type = settings.DB_TYPE
        if db_type == "postgresql":
            self.engine = sqlalchemy.create_engine(
                f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
            )
        elif db_type == "duckdb":
            self.engine = sqlalchemy.create_engine("duckdb:///analyticsai.db")
        # Add other DBs as needed

    def query(self, sql: str):
        with self.engine.connect() as conn:
            result = conn.execute(sql)
            return [dict(row) for row in result]

    # Example: adapter for external API
    def fetch_from_salesforce(self, endpoint: str):
        api_key = settings.SALESFORCE_API_KEY
        # Placeholder: implement actual Salesforce API call
        return {"status": "success", "endpoint": endpoint}

# Usage: adapter = DataAdapter(); adapter.query("SELECT * FROM sales")