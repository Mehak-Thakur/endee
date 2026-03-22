import streamlit as st
from src.parser import extract_text
from src.embeddings import get_embedding
from src.matcher import calculate_similarity, find_missing_skills, generate_suggestions
from src.endee_db import EndeeDB

# Initialize Endee DB
db = EndeeDB()

st.set_page_config(page_title="AI Resume Matcher", layout="centered")

st.title("AI Resume Matcher")
st.write("Match your resume with job description using AI & Vector Search")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume_file and job_desc:

        # Extract resume text
        resume_text = extract_text(resume_file)

        # Generate embeddings
        resume_emb = get_embedding(resume_text)
        jd_emb = get_embedding(job_desc)

        # Store in Endee (Vector DB)
        db.insert("resume", resume_emb, {"type": "resume"})
        db.insert("job_desc", jd_emb, {"type": "job_description"})

        # Perform similarity (vector search concept)
        score = calculate_similarity(resume_emb, jd_emb)

        # Find missing skills
        missing_skills = find_missing_skills(resume_text, job_desc)

        # Generate suggestions
        suggestions = generate_suggestions(missing_skills)

        # OUTPUT
        st.subheader(" Match Score")
        st.success(f"{score}% match")

        st.subheader(" Missing Skills")
        if missing_skills:
            st.write(", ".join(missing_skills))
        else:
            st.write("No major missing skills detected")

        st.subheader(" Suggestions")
        for s in suggestions:
            st.write("- " + s)

    else:
        st.warning("Please upload resume and enter job description")
