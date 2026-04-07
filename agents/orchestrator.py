from agents.tutor_agent import TutorAgent
from agents.quiz_agent import QuizAgent
from agents.evaluator_agent import EvaluatorAgent


class StudySession:

    def __init__(self, transcript, vector_db):

        self.transcript = transcript
        self.db = vector_db

        self.tutor = TutorAgent(vector_db)

        self.quiz_agent = QuizAgent(transcript)

        self.evaluator = EvaluatorAgent()

    def ask_question(self, question):

        return self.tutor.answer_question(question)

    def generate_quiz(self):

        return self.quiz_agent.create_quiz()

    def grade_quiz(self, user_answers):

        correct = self.quiz_agent.get_answers()

        return self.evaluator.grade(user_answers, correct)