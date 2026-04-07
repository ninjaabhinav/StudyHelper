class SessionState:

    def __init__(self):
        self.transcript = None
        self.chunks = None
        self.vector_db = None
        self.notes_pdf = None
        self.quiz_questions = []
        self.quiz_answers = []