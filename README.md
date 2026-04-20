# AI Research Paper Assistant 📄🤖

An AI-powered web application that helps researchers, students, and developers quickly understand research papers.

The system allows users to upload a research paper (PDF) and automatically generate **structured summaries, key insights, and interactive Q&A** using modern AI models.

This project integrates **Natural Language Processing (NLP), Large Language Models (LLMs), and Semantic Search** to simplify academic research.

---

## 🚀 Project Overview

Reading research papers is time-consuming. This tool simplifies the process by:

* 📄 Extracting text from research papers
* 🤖 Generating structured AI summaries
* 📊 Highlighting key findings with data (percentages, stats)
* 💡 Explaining important concepts
* 💬 Allowing users to ask questions about the paper

👉 The assistant acts like a **mini AI research analyst**.

---

## ✨ Features

### 1. 📂 PDF Upload

Upload research papers in PDF format.

### 2. 🧠 AI Generated Summary

Generates:

* Short summary
* Key contributions
* Important concepts
* Data-driven insights

### 3. 💬 Chat with Research Paper

Ask questions like:

* What is the methodology used?
* What are the key findings?
* What problem does the paper solve?

### 4. 🔍 Semantic Search

* Uses vector embeddings + FAISS
* Finds relevant sections from the document

### 5. 📚 Literature Understanding

* Explains complex research ideas in simple terms

### 6. 🧾 Citation Extraction

* Automatically generates APA/IEEE citations

---

## 🧠 System Architecture

```
PDF Upload
      ↓
PDF Text Extraction
      ↓
Text Processing
      ↓
Vector Embeddings (FAISS)
      ↓
LLM (Groq API)
      ↓
Summary / Q&A / Insights
      ↓
Streamlit UI
```

---

## 📁 Project Structure

```
AI-Research-Assistant/
│
├── app.py
├── pdf_reader.py
├── summarizer.py
├── chat_with_paper.py
├── embeddings.py
├── citation.py
│
├── requirements.txt
├── README.md
└── .env (not included)
```

---

## 🛠️ Technologies Used

### 💻 Programming Language

* Python

### 📚 Libraries & Tools

* Streamlit (UI)
* PyPDF (PDF extraction)
* Sentence Transformers (embeddings)
* FAISS (vector search)
* NumPy
* python-dotenv

### 🤖 AI Model

* Groq API (LLaMA 3.1 models)

---

## 🔥 Why Groq Instead of Ollama?

| Feature       | Ollama ❌   | Groq ✅         |
| ------------- | ---------- | -------------- |
| Installation  | Required   | Not needed     |
| Setup Time    | High       | Minimal        |
| Speed         | Medium     | Very Fast ⚡    |
| Accessibility | Local only | Works anywhere |

---

## 🔑 Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Amrutha-Pawar/AI-Research-Papers.git
cd AI-Research-Papers
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

👉 Get API key: https://console.groq.com

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

## 📊 Example Output

The system generates structured insights such as:

* 📌 Summary
* 🎯 Research Objective
* 📊 Key Findings (with percentages/data)
* 💡 Contributions
* 🌍 Real-world impact

---

## 🎯 Use Cases

### 👩‍🎓 For Students

* Quickly understand research papers
* Generate summaries for assignments

### 🔬 For Researchers

* Speed up literature reviews
* Extract insights efficiently

### 👨‍💻 For Developers

* Learn AI-powered document analysis
* Build NLP-based applications

---

## 🚀 Future Improvements

* Multi-paper analysis
* Research comparison tool
* Automatic literature review generator
* Knowledge graph visualization
* Paper recommendation system

---

## 📚 Learning Outcomes

This project demonstrates:

* Natural Language Processing
* Large Language Models (LLMs)
* Vector Search (FAISS)
* AI-powered document processing
* Full-stack AI application development

---

## 👩‍💻 Author

**Pawar Amrutha**
BTech Computer Science and Engineering

### Interests:

* Artificial Intelligence
* Web Development
* AI-powered Applications

---

## 📄 License

This project is open-source and available for educational and research purposes.
