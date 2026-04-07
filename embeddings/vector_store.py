from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from embeddings.embedder import get_embedding_model

def create_vector_store(chunks):

    embeddings = get_embedding_model()

    db = FAISS.from_texts(chunks, embeddings)

    return db


def search(db, query, k=4):

    docs = db.similarity_search(query, k=k)

    return docs