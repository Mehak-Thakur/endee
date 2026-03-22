# AI Resume Matcher using Endee

## 📌 Overview
This project is an AI-powered Resume Matcher that compares resumes with job descriptions using semantic similarity and vector search.

## 💡 Problem Statement
Recruiters spend significant time manually screening resumes. This system automates the process using AI and vector embeddings.

## 🚀 Features
- Upload Resume (PDF)
- Input Job Description
- Generate embeddings
- Store vectors using Endee
- Compute match score
- Identify missing skills
- Provide suggestions

## 🧠 System Design
Resume / JD → Embeddings → Endee Vector DB → Similarity Search → Output

## ⚙️ Tech Stack
- Python
- Streamlit
- Sentence Transformers
- Endee (Vector DB)

## 🧩 Endee Usage
Endee is used as a vector storage layer to store embeddings and simulate retrieval-based similarity search.

## ▶️ Run Project
pip install -r requirements.txt  
streamlit run app.py

## 📊 Output
- Match Score (%)
- Missing Skills
- Suggestions