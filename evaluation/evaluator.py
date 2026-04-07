import re

def parse_quiz(quiz_text):

    questions = []
    answers = []
    options_list = []
    topics = []

    blocks = re.split(r"\n\s*Question\s*\d+", quiz_text, flags=re.IGNORECASE)

    for block in blocks[1:]:

        lines = [l.strip() for l in block.split("\n") if l.strip()]

        question = ""
        topic = "General"
        options = {}
        correct = None

        for line in lines:

            if line.lower().startswith("topic"):
                topic = line.split(":",1)[1].strip()

            elif line.lower().startswith("question"):
                question = line.split(":",1)[1].strip()

            elif line.startswith("A)"):
                options["A"] = line.split(")",1)[1].strip()

            elif line.startswith("B)"):
                options["B"] = line.split(")",1)[1].strip()

            elif line.startswith("C)"):
                options["C"] = line.split(")",1)[1].strip()

            elif line.startswith("D)"):
                options["D"] = line.split(")",1)[1].strip()

            elif line.lower().startswith("answer"):
                correct = line.split(":")[1].strip()[0]

        questions.append(question)
        options_list.append(options)
        answers.append(correct)
        topics.append(topic)

    return questions, options_list, answers, topics


def evaluate(user_answers, correct_answers):
    """
    Compare user answers with correct answers
    """

    score = 0

    for user, correct in zip(user_answers, correct_answers):

        if correct is None:
            continue

        if user.upper() == correct:
            score += 1

    return score

def topic_analysis(user_answers, correct_answers, topics):

    topic_stats = {}

    for ua, ca, topic in zip(user_answers, correct_answers, topics):

        if topic not in topic_stats:
            topic_stats[topic] = {"correct": 0, "total": 0}

        topic_stats[topic]["total"] += 1

        if ua == ca:
            topic_stats[topic]["correct"] += 1

    strong = []
    weak = []

    for topic, stats in topic_stats.items():

        accuracy = stats["correct"] / stats["total"]

        if accuracy >= 0.7:
            strong.append(topic)
        else:
            weak.append(topic)

    return strong, weak