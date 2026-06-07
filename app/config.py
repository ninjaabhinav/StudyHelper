import os
from dotenv import load_dotenv

load_dotenv()

os.environ["TRANSFORMERS_OFFLINE"] = "0"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

hf_token = os.getenv("HF_TOKEN", "")
if hf_token:
    os.environ["HUGGINGFACE_HUB_TOKEN"] = hf_token

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    CHUNK_SIZE = 1200
    CHUNK_OVERLAP = 200
    TOP_K_RESULTS = 4