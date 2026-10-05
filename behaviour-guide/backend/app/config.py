import os

from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "")
LLM_MODEL = os.getenv("LLM_MODEL", "")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
CHROMA_PATH = os.getenv("CHROMA_PATH", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")
