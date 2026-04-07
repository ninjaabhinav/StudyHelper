TOPIC_EXTRACTION_PROMPT = """
You are analyzing a lecture transcript.

Identify the main topics discussed.

Return ONLY a numbered list.

Transcript:
{transcript}
"""


SUMMARY_PROMPT = """
Create structured study notes from this lecture transcript.

Rules:
- Use headings
- Use bullet points
- Keep explanations concise

Transcript:
{transcript}
"""


QUIZ_PROMPT = """
Generate multiple choice questions from the lecture.

Rules:
- Only use information from transcript
- 4 options per question
- Mark correct answer

Format:

Question:
A)
B)
C)
D)

Answer:
"""


TUTOR_PROMPT = """
You are an AI tutor helping a student.

Use the lecture transcript first.
Use web information only if needed.

QUESTION:
{question}

LECTURE:
{context}

WEB:
{web}
"""