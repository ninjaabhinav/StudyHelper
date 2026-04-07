from langchain_groq import ChatGroq
from app.config import Config


def generate_answer(question, transcript_context, web_context):

    llm = ChatGroq(
    api_key=Config.GROQ_API_KEY,
    model="llama-3.1-8b-instant"
    )

    prompt = f"""
You are an AI tutor helping a student understand a lecture.

Use the lecture transcript as the primary source.

If the lecture explanation is incomplete,
use web information to clarify concepts.

Provide a clear explanation.

QUESTION:
{question}

LECTURE CONTEXT:
{transcript_context}

WEB CONTEXT:
{web_context}
"""

    response = llm.invoke(prompt)

    return response.content