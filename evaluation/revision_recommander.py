def recommend_revision(weak_topics):

    if not weak_topics:

        return "Excellent performance. No major weak areas."

    message = "\nYou should revise the following topics:\n"

    for topic in weak_topics:
        message += f"- {topic}\n"

    return message