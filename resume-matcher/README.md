# AI Resume Matcher using Endee (Vector Database)

## Project Overview

The **AI Resume Matcher** is a semantic search-based application that compares a candidate’s resume with a job description using advanced Natural Language Processing (NLP) techniques.

This system leverages **vector embeddings and similarity search** to automate resume screening, helping recruiters quickly identify the most suitable candidates.

---

## Problem Statement

Recruiters often spend significant time manually reviewing resumes to match them with job descriptions. This process is:

* Time-consuming
* Prone to human bias
* Inefficient at scale

This project solves the problem by using **AI-powered semantic similarity** to automatically evaluate resume-job compatibility.

---

## Solution Approach

The system converts both the resume and job description into **vector embeddings** and performs **semantic similarity search** using a vector database.

It provides:

*  Match Score (percentage similarity)
*  Missing Skills
*  Suggestions for improvement

---

## Key Features

* Upload Resume (PDF format)
* Input Job Description
* Transformer-based embedding generation
* Vector storage using Endee
* Semantic similarity computation
* Missing skills identification
* Intelligent suggestions

---

## System Architecture

```
Resume (PDF) + Job Description
            ↓
     Text Extraction (PDF Parser)
            ↓
     Text Embedding (Sentence Transformers)
            ↓
     Vector Storage (Endee Database)
            ↓
     Similarity Search (Cosine Similarity)
            ↓
     Match Score + Insights
```

---

## Tech Stack

| Component       | Technology                       |
| --------------- | -------------------------------- |
| Language        | Python                           |
| UI              | Streamlit                        |
| NLP Model       | Sentence Transformers            |
| Vector Database | Endee                            |
| PDF Processing  | pdfplumber                       |
| Similarity      | Scikit-learn (Cosine Similarity) |

---

## Endee Integration (Core Requirement)

This project uses **Endee as a vector database** to:

* Store embeddings of resumes and job descriptions
* Enable vector-based retrieval
* Support semantic similarity search

Since Endee is not distributed as a pip package, the repository was **forked and used as the base**, and a lightweight abstraction layer (`EndeeDB`) is implemented to simulate vector storage and retrieval aligned with Endee’s architecture.

---

## Project Structure

```
endee/
│
├── resume-matcher/
│   │
│   ├── app.py                # Streamlit UI and main logic
│   ├── requirements.txt     # Project dependencies
│   ├── README.md            # Documentation
│   │
│   ├── src/
│   │   ├── parser.py        # Resume text extraction
│   │   ├── embeddings.py    # Embedding generation
│   │   ├── matcher.py       # Similarity + skill analysis
│   │___├── endee_db.py      # Endee vector storage layer
│ 
│
│
└── (Original Endee repository files)
```

---

## Setup & Execution Instructions

### 🔹 1. Clone Repository

```
git clone https://github.com/Mehak-Thakur/endee.git
cd endee/resume-matcher
```

---

### 🔹 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 🔹 3. Run Application

```
streamlit run app.py
```

---

### 🔹 4. Open in Browser

Streamlit will automatically open:

```
http://localhost:8501
```

---

##  Output Example

The system provides:

* Match Score (e.g., 82%)
* Missing Skills (e.g., SQL, NLP)
* Suggestions for improvement

---


## 🔥 Future Enhancements

* Advanced NLP-based skill extraction (spaCy)
* Multiple resume ranking system
* Keyword highlighting
* Deployment on cloud (Streamlit Cloud / AWS)
* Integration with real job portals

---

##  Use Cases

* Automated resume screening
* Recruitment assistance tools
* Career guidance platforms
* Job recommendation systems

---

## Author

**Mehak Thakur**

---

## Acknowledgment

This project is built using the **Endee Vector Database** repository as a base for implementing vector search functionality.

---
