def run_quiz(questions):

    print("\nStarting Quiz")
    print("Type A/B/C/D. Type 'stop' to end.\n")

    user_answers = []

    for q in questions:

        print("Question:")
        print(q.split("Answer:")[0])

        user = input("Your answer: ")

        if user.lower() == "stop":
            break

        user_answers.append(user)

    return user_answers