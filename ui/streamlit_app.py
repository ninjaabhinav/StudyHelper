import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st

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
from evaluation.evaluator import parse_quiz
from evaluation.evaluator import evaluate
from evaluation.evaluator import topic_analysis

st.set_page_config(
    page_title="StudyHelper",
    page_icon="📚",
    layout="wide"
)

st.title("StudyHelper AI Tutor")

# session state
if "db" not in st.session_state:
    st.session_state.db = None

if "transcript" not in st.session_state:
    st.session_state.transcript = None

if "notes_pdf" not in st.session_state:
    st.session_state.notes_pdf = None


# -------------------
# VIDEO INPUT
# -------------------

video_url = st.text_input("Enter YouTube Lecture URL")

if st.button("Process Video"):

    with st.spinner("Processing video..."):

        transcript = load_transcript(video_url)

        clean_text = clean_transcript(transcript)

        chunks = create_chunks(clean_text)

        db = create_vector_store(chunks)

        notes = summarize_transcript(clean_text)

        pdf_path = generate_pdf(notes)

        st.session_state.db = db
        st.session_state.transcript = clean_text
        st.session_state.notes_pdf = pdf_path

    st.success("Video processed successfully")

    with open(pdf_path, "rb") as f:
        st.download_button(
            label="Download Lecture Notes",
            data=f,
            file_name="lecture_notes.pdf",
            mime="application/pdf"
        )


# -------------------
# Q&A SECTION
# -------------------

st.header("💬 AI Tutor")

chat_container = st.container()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with chat_container:

    for msg in st.session_state.chat_history:

        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["content"])
        else:
            with st.chat_message("assistant"):
                st.markdown(msg["content"])


user_input = st.text_input("Ask something about the lecture")

if st.button("Send"):

    if st.session_state.db is None:
        st.warning("Please process a video first.")
    else:

        context = retrieve_context(
            st.session_state.db,
            user_input
        )

        web = search_web(user_input)

        answer = generate_answer(
            user_input,
            context,
            web
        )

        st.session_state.chat_history.append(
            {"role": "user", "content": user_input}
        )

        st.session_state.chat_history.append(
            {"role": "assistant", "content": answer}
        )

        st.rerun()
# -------------------
# QUIZ SECTION
# -------------------

st.subheader("Quiz")

if st.button("Generate Quiz"):

    quiz_text = generate_quiz(
        st.session_state.transcript
    )

    questions, options_list, answers, topics = parse_quiz(quiz_text)

    st.session_state.quiz_questions = questions
    st.session_state.quiz_options = options_list
    st.session_state.quiz_answers = answers
    st.session_state.quiz_topics = topics

# Display quiz questions
user_answers = []

if "quiz_questions" in st.session_state:

    for i, q in enumerate(st.session_state.quiz_questions):

        st.markdown(f"### Question {i+1}")

        st.write(q)

        options = st.session_state.quiz_options[i]

        ans = st.radio(
            "Select answer",
            ["A", "B", "C", "D"],
            format_func=lambda x: f"{x}) {options.get(x,'')}",
            key=i
        )

        user_answers.append(ans)

    if st.button("Submit Quiz"):

        score = evaluate(user_answers, st.session_state.quiz_answers)

        strong, weak = topic_analysis(
            user_answers,
            st.session_state.quiz_answers,
            st.session_state.quiz_topics
        )

        st.success(f"Score: {score}/{len(user_answers)}")

        st.subheader("Concept Analysis")

        st.write("Strong Topics:")
        for t in strong:
            st.write("✅", t)

        st.write("Needs Revision:")
        for t in weak:
            st.write("⚠️", t)