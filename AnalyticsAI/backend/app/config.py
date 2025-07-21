import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # LLM
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")
    # Database
    DB_TYPE = os.getenv("DB_TYPE", "duckdb")  # Options: duckdb, postgresql, mysql
    DB_PATH = os.getenv("DB_PATH", "analyticsai.db")
    DB_HOST = os.getenv("DB_HOST", "")
    DB_PORT = os.getenv("DB_PORT", "")
    DB_USER = os.getenv("DB_USER", "")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "")
    # External APIs
    SALESFORCE_API_KEY = os.getenv("SALESFORCE_API_KEY", "")
    GOOGLE_ANALYTICS_API_KEY = os.getenv("GOOGLE_ANALYTICS_API_KEY", "")
    # General
    ENV = os.getenv("ENV", "dev")
    DEBUG = os.getenv("DEBUG", "true") == "true"

settings = Settings()