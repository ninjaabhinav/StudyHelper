class Question:

    def __init__(self, text, options, answer):

        self.text = text
        self.options = options
        self.answer = answer


class QuestionBank:

    def __init__(self):

        self.questions = []

    def add(self, question):

        self.questions.append(question)

    def get_all(self):

        return self.questions

    def size(self):

        return len(self.questions)