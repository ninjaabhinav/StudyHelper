import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    EMBEDDING_MODEL = "BAAI/bge-small-en"

    CHUNK_SIZE = 1200
    CHUNK_OVERLAP = 200

    TOP_K_RESULTS = 4