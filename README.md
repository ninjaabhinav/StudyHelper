# 📚 StudyHelper

🚀 AI-powered learning assistant that transforms YouTube lectures into summaries, Q&A, and quizzes using LLMs and Retrieval-Augmented Generation (RAG).

---

## 🧩 Problem It Solves

Students spend hours watching long YouTube lectures but struggle to:
- Retain key concepts  
- Quickly revise content  
- Test their understanding  

StudyHelper solves this by converting video content into **structured learning outputs**:
- Concise summaries  
- Context-aware Q&A  
- Auto-generated quizzes  

This reduces passive watching and enables **active learning**.

---

## ⚙️ How It Works

StudyHelper implements a full **GenAI pipeline** combining transcript extraction, retrieval, and LLM-based generation.

### 🔄 Pipeline Overview

1. Extract transcript from YouTube video  
2. Process and chunk the text  
3. Store embeddings for retrieval  
4. Use RAG to answer questions contextually  
5. Generate summaries and quizzes using LLM  

---

## 🧠 Core Technologies

- **RAG (Retrieval-Augmented Generation)** – Enables context-aware responses  
- **Groq API** – Fast LLM inference for generation tasks  
- **YouTube Transcript API** – Fetches video transcripts automatically  

---

## 🎯 Key Features

- 🎥 **YouTube Transcript Extraction**  
  Automatically pulls transcript from any lecture video  

- 📝 **Smart Summarization**  
  Converts long content into concise notes  

- ❓ **RAG-based Q&A**  
  Ask questions and get answers grounded in video context  

- 🧪 **Quiz Generation**  
  Generates questions to test understanding  

- ⚡ **Fast Inference with Groq**  
  Low-latency responses for better UX  

---

## 👥 Who Would Use It

- Students preparing from YouTube lectures  
- EdTech startups building AI learning tools  
- Self-learners who want faster revision and comprehension  

---

## 📊 Example Use Case

- Input: YouTube lecture link  
- Output:
  - Summary of key concepts  
  - Ability to ask questions about the lecture  
  - Auto-generated quiz for practice  

---

## 🧠 System Design (High-Level)
User Input (YouTube URL)  
↓  
Transcript Extraction (YouTube API)  
↓  
Text Chunking + Embeddings  
↓  
Vector Retrieval (RAG)  
↓  
LLM (Groq)  
↓  
Outputs: Summary | Q&A | Quiz  


---

## 🛠️ Tech Stack

- Python  
- LangChain  
- Groq API  
- YouTube Transcript API  
- Vector-based retrieval (RAG pipeline)  

---

## 📌 Future Improvements

- Multi-video knowledge base support  
- PDF / document upload integration  
- Personalized learning paths  
- UI/UX improvements for better interaction  

---

## 📬 Contact

**Abhinav Mishra**  
GitHub: https://github.com/ninjaabhinav    

---

## 📄 License

This project is open-source and available under the MIT License.
