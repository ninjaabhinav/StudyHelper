from langchain_groq import ChatGroq
from app.config import Config


def extract_topics(transcript):

    llm = ChatGroq(
        groq_api_key=Config.GROQ_API_KEY,
        model="llama-3.1-8b-instant"
    )

    prompt = f"""
You are analyzing a lecture transcript.

Identify the main topics covered in the lecture.

Return ONLY a numbered list of topics.

Transcript:
{transcript[:12000]}
"""

    response = llm.invoke(prompt)

    topics = response.content.split("\n")

    topics = [t.strip() for t in topics if t.strip()]

    return topics