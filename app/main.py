from ingestion.youtube_loader import load_transcript
from ingestion.transcript_cleaner import clean_transcript
from ingestion.chunker import create_chunks
from embeddings.vector_store import create_vector_store

from notes.topic_extractor import extract_topics
from notes.summarizer import summarize_transcript
from notes.pdf_generator import generate_pdf

from qa.retriever import retrieve_context
from qa.web_search import search_web
from qa.answer_generator import generate_answer

from quiz.quiz_generator import generate_quiz
from quiz.quiz_session import run_quiz

from evaluation.evaluator import parse_quiz, evaluate


def run():

    # -----------------------------
    # VIDEO INGESTION PIPELINE
    # -----------------------------
    url = input("Enter YouTube URL: ")

    transcript = load_transcript(url)

    clean_text = clean_transcript(transcript)

    chunks = create_chunks(clean_text)

    db = create_vector_store(chunks)

    print(type(db))

    # # Test retrieval
    # docs = db.similarity_search("What is this video about?", k=3)

    # for d in docs:
    #     print("\n--- Retrieved Chunk ---\n")
    #     print(d.page_content[:200])

    # -----------------------------
    # NOTES GENERATION
    # -----------------------------
    print("\nGenerating lecture notes...")

    topics = extract_topics(clean_text)

    notes = summarize_transcript(clean_text)

    pdf_path = generate_pdf(notes)

    print("Lecture notes generated.")

    print("\nTopics detected:")

    for t in topics:
        print(t)

    print(f"\nPDF saved at: {pdf_path}")

    # -----------------------------
    # TUTOR Q&A LOOP
    # -----------------------------
    print("\nTutor ready. Ask questions about the lecture.")
    print("Type 'exit' to stop.\n")

    while True:

        question = input("Question: ")

        if question.lower() == "exit":
            break

        transcript_context = retrieve_context(db, question)

        web_context = search_web(question)

        answer = generate_answer(
            question,
            transcript_context,
            web_context
        )

        print("\nAnswer:\n")
        print(answer)

    # -----------------------------
    # QUIZ SECTION
    # -----------------------------
    mode = input("\nDo you want to take a quiz? (yes/no): ")

    if mode.lower() != "yes":
        print("Session finished.")
        return

    print("\nGenerating quiz...\n")

    quiz_text = generate_quiz(clean_text)

    print(quiz_text)

    # -----------------------------
    # PARSE QUIZ
    # -----------------------------
    questions, correct_answers = parse_quiz(quiz_text)

    if not questions:
        print("\nQuiz parsing failed.")
        return

    # -----------------------------
    # RUN QUIZ
    # -----------------------------
    user_answers = run_quiz(questions)

    if not user_answers:
        print("\nQuiz cancelled.")
        return

    # -----------------------------
    # EVALUATE QUIZ
    # -----------------------------
    score = evaluator(user_answers, correct_answers)

    print(f"\nYour score: {score}/{len(user_answers)}")


if __name__ == "__main__":
    run()