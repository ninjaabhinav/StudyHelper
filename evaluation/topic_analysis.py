def analyze_topics(user_answers, correct_answers, topics):

    topic_results = {}

    for i in range(len(user_answers)):

        topic = topics[i % len(topics)]

        correct = user_answers[i].upper() == correct_answers[i]

        if topic not in topic_results:
            topic_results[topic] = []

        topic_results[topic].append(correct)

    weak_topics = []

    for topic, results in topic_results.items():

        accuracy = sum(results) / len(results)

        if accuracy < 0.5:
            weak_topics.append(topic)

    return weak_topics