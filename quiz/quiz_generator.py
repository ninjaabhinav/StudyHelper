from langchain_groq import ChatGroq
from app.config import Config


def generate_quiz(transcript):

    llm = ChatGroq(
    api_key=Config.GROQ_API_KEY,
    model="llama-3.1-8b-instant"
    )

    prompt = f"""
You are generating a quiz from a lecture transcript.

Generate 5 multiple choice questions based ONLY on the lecture.

Rules:
- Each question must have exactly 4 options.
- Each question must include a topic.
- The correct answer should vary between A, B, C, and D.
- Do NOT reveal the answer inside the options.
- Options must only contain the option text.

Return EXACTLY in the following format:

Question 1
Topic: <topic name>
Question: <question text>

A) <option text>
B) <option text>
C) <option text>
D) <option text>

Answer: <A or B or C or D>

Question 2
Topic: <topic name>
Question: <question text>

A) <option text>
B) <option text>
C) <option text>
D) <option text>

Answer: <A or B or C or D>

Question 3
Topic: <topic name>
Question: <question text>

A) <option text>
B) <option text>
C) <option text>
D) <option text>

Answer: <A or B or C or D>

IMPORTANT:
- Never include the word "Answer" inside options.
- Only the final line should contain the answer.
- The answer letter must vary across questions.

Transcript:
{transcript[:12000]}
"""

    response = llm.invoke(prompt)
    quiz_text = response.content

    # Remove leaked answers from options
    quiz_text = quiz_text.replace("A) Answer:", "A)")
    quiz_text = quiz_text.replace("B) Answer:", "B)")
    quiz_text = quiz_text.replace("C) Answer:", "C)")
    quiz_text = quiz_text.replace("D) Answer:", "D)")

    return quiz_text