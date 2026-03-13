AI Research Paper Assistant 📄🤖

An AI-powered web application that helps researchers, students, and developers quickly understand research papers.
The system allows users to upload a research paper (PDF) and automatically generate summaries, extract key insights, and interact with the paper using AI.

This project integrates Natural Language Processing (NLP), Large Language Models (LLMs), and Semantic Search to assist with academic research.

Project Overview

Reading research papers is time-consuming. This tool simplifies the process by:

Extracting text from research papers

Generating AI summaries

Identifying key contributions

Explaining important concepts

Allowing users to ask questions about the paper

The assistant acts like a mini AI research analyst that helps understand complex academic papers quickly.

Features
1. PDF Upload

Users can upload research papers in PDF format.

2. AI Generated Summary

The system automatically generates:

Short summary

Key contributions

Important concepts

3. Chat with Research Paper

Users can ask questions such as:

What is the methodology used in this paper?

What are the key findings?

What problem does the research solve?

4. Semantic Search

The system performs vector-based search within the document to find relevant sections.

5. Literature Understanding

AI helps explain difficult concepts and research ideas.

6. Citation Extraction

Automatically generates academic citations (APA/IEEE style).

System Architecture

Workflow of the system:

PDF Upload
      ↓
PDF Text Extraction
      ↓
Text Processing
      ↓
AI Model (LLM)
      ↓
Summary / Answer Generation
      ↓
User Interface (Streamlit)
Project Structure
AI-Research-Assistant
│
├── app.py
├── pdf_reader.py
├── summarizer.py
├── chat_with_paper.py
├── embeddings.py
├── citation.py
│
├── papers
│
├── requirements.txt
└── README.md
Technologies Used
Programming Language

Python

Libraries and Tools

Streamlit (Web Interface)

PyPDF (PDF text extraction)

Ollama (Local LLM execution)

Sentence Transformers

FAISS (Semantic Search)

NumPy

AI Model

Phi-3 Mini (via Ollama)

Installation Guide
1. Clone the Repository
git clone https://github.com/yourusername/AI-Research-Assistant.git
cd AI-Research-Assistant
2. Create Virtual Environment
python -m venv venv

Activate it:

Windows

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

Or install manually:

pip install streamlit pypdf ollama sentence-transformers faiss-cpu
4. Install Ollama

Download and install Ollama from:

https://ollama.com

5. Download AI Model
ollama pull phi3:mini
Running the Application

Start the web application:

streamlit run app.py

Then open the browser:

http://localhost:8501

Upload a research paper and start exploring the AI features.

Example Use Cases
For Students

Quickly understand research papers

Generate summaries for assignments

Understand difficult concepts

For Researchers

Speed up literature reviews

Extract insights from papers

For Developers

Learn about AI-powered document analysis systems

Example Output

AI generates structured results such as:

Summary

Overview of the research problem

Key findings of the paper

Key Contributions

Main innovations of the research

Important Concepts

Core ideas used in the study

Future Improvements

Planned enhancements:

Multi-paper analysis

Research paper comparison

Automatic literature review generation

Knowledge graph of research topics

Citation network visualization

Research idea generator

Paper recommendation system

Learning Outcomes

This project demonstrates knowledge of:

Natural Language Processing

Large Language Models

Vector Search

AI-powered document processing

Python backend development

AI web application development

Author

Pawar Amrutha
BTech Computer Science and Engineering

Interests:

Artificial Intelligence

Web Development

AI-powered Applications

License

This project is open-source and available for educational and research purposes.