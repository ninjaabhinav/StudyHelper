from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import Config


def create_chunks(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=Config.CHUNK_SIZE,
        chunk_overlap=Config.CHUNK_OVERLAP
    )

    chunks = splitter.split_text(text)

    return chunks