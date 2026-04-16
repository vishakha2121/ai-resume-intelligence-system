import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///../database/resume_intelligence.db")
    MODEL_NAME = os.getenv("MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2")
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
    UPLOAD_DIR = "uploads"
    LOG_DIR = "logs"

config = Config()