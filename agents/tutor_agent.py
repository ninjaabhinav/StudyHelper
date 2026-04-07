from qa.retriever import retrieve_context
from qa.web_search import search_web
from qa.answer_generator import generate_answer


class TutorAgent:

    def __init__(self, vector_db):

        self.db = vector_db

    def answer_question(self, question):

        transcript_context = retrieve_context(self.db, question)

        web_context = search_web(question)

        response = generate_answer(
            question,
            transcript_context,
            web_context
        )

        return response