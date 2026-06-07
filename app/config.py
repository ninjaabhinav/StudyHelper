import os
os.environ["HF_ENDPOINT"] = "https://huggingface.co"
os.environ["TRANSFORMERS_OFFLINE"] = "0"
os.environ["HUGGINGFACE_HUB_TOKEN"] = os.getenv("HF_TOKEN", "")
from dotenv import load_dotenv

load_dotenv()

class Config:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    EMBEDDING_MODEL = "all-MiniLM-L6-v2"

    CHUNK_SIZE = 1200
    CHUNK_OVERLAP = 200

    TOP_K_RESULTS = 4