from evaluation.evaluator import evaluate


class EvaluatorAgent:

    def __init__(self):

        self.score = 0

    def grade(self, user_answers, correct_answers):

        self.score = evaluate(user_answers, correct_answers)

        return self.score