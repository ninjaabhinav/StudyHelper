from quiz.quiz_generator import generate_quiz
from evaluation.evaluator import parse_quiz


class QuizAgent:

    def __init__(self, transcript):

        self.transcript = transcript

        self.quiz_text = None
        self.questions = None
        self.answers = None

    def create_quiz(self):

        self.quiz_text = generate_quiz(self.transcript)

        self.questions, self.answers = parse_quiz(self.quiz_text)

        return self.questions

    def get_answers(self):

        return self.answers