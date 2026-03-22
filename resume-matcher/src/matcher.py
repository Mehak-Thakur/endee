from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_emb, jd_emb):
    score = cosine_similarity([resume_emb], [jd_emb])[0][0]
    return round(score * 100, 2)


def find_missing_skills(resume_text, jd_text):
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())

    missing = jd_words - resume_words

    # Filter useful words
    filtered = [word for word in missing if len(word) > 3]

    return filtered[:15]


def generate_suggestions(missing_skills):
    suggestions = []
    for skill in missing_skills[:5]:
        suggestions.append(f"Consider improving or adding skill: {skill}")
    return suggestions