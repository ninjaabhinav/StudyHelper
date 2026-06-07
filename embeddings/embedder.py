from langchain_huggingface import HuggingFaceEmbeddings
from app.config import Config
import os

_embedding_model = None

def get_embedding_model():
    global _embedding_model

    if _embedding_model is None:
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        _embedding_model = HuggingFaceEmbeddings(
            model_name=Config.EMBEDDING_MODEL,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
            cache_folder="/tmp/hf_cache"
        )

    return _embedding_model