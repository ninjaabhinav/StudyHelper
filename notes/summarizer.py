from langchain_groq import ChatGroq
from utils.text_utils import split_into_blocks
from app.config import Config


def summarize_transcript(transcript):

    llm = ChatGroq(
    api_key=Config.GROQ_API_KEY,
    model="llama-3.1-8b-instant"
    )

    blocks = split_into_blocks(transcript, 8000)

    summaries = []

    for block in blocks:

        prompt = f"""
Create structured study notes from this lecture section.

Use:
- headings
- bullet points
- short explanations

Text:
{block}
"""

        response = llm.invoke(prompt)

        summaries.append(response.content)

    final_prompt = f"""
Combine the following section summaries into a clean lecture note.

{summaries}
"""

    final_notes = llm.invoke(final_prompt)

    return final_notes.content