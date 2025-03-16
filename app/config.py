import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration settings."""
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/scamdb")
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    HUGGINGFACE_MODEL = os.getenv("HUGGINGFACE_MODEL", "ml6team/roberta-base-cls-phishing")
