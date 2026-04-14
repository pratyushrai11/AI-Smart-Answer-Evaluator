import streamlit as st
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="AI Smart Answer Evaluator", layout="wide")

# ------------------ CSS ------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #e2e8f0;
}
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #38bdf8;
}
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 20px;
}
.card {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 15px;
}
textarea {
    background-color: #ffffff !important;
    color: black !important;
    border-radius: 10px !important;
}
.stButton>button {
    background: linear-gradient(45deg, #38bdf8, #06b6d4);
    color: black;
    font-weight: bold;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="title">🤖 AI Smart Answer Evaluator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Advanced NLP Based Evaluation System</div>', unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.header("⚙️ Settings")

max_marks = st.sidebar.slider("Maximum Marks", 5, 20, 10)
w1 = st.sidebar.slider("Similarity Weight", 0.0, 1.0, 0.5)
w2 = st.sidebar.slider("Keyword Weight", 0.0, 1.0, 0.3)
w3 = st.sidebar.slider("Length Weight", 0.0, 1.0, 0.2)

total = w1 + w2 + w3
w1, w2, w3 = w1/total, w2/total, w3/total

# ------------------ INFO PANEL ------------------
st.info("""
📌 This system evaluates answers using:
- Cosine Similarity (TF-IDF)
- Keyword Matching
- Length Analysis
- Weighted Final Score
""")

# ------------------ INPUT ------------------
col1, col2 = st.columns(2)

with col1:
    model_answer = st.text_area("📘 Model Answer", height=200)

with col2:
    student_answer = st.text_area("🧑‍🎓 Student Answer", height=200)

# ------------------ FUNCTIONS ------------------
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

def keyword_match(model, student):
    m = set(model.split())
    s = set(student.split())
    common = m.intersection(s)
    return len(common)/len(m) if m else 0, common

def length_score(model, student):
    return min(len(student.split())/len(model.split()), 1)

def similarity(model, student):
    vec = TfidfVectorizer()
    vectors = vec.fit_transform([model, student])
    return cosine_similarity(vectors[0], vectors[1])[0][0]

# ------------------ BUTTONS ------------------
colA, colB, colC, colD = st.columns(4)

eval_btn = colA.button("🚀 Evaluate")
sample_btn = colB.button("📄 Sample")
clear_btn = colC.button("🧹 Clear")
show_keywords_btn = colD.button("🔍 Show Keywords")

# ------------------ SAMPLE ------------------
if sample_btn:
    model_answer = "Normalization reduces redundancy and improves data integrity."
    student_answer = "Normalization removes duplicate data and improves consistency."
    st.success("Sample Loaded")

# ------------------ CLEAR ------------------
if clear_btn:
    st.rerun()

# ------------------ EVALUATION ------------------
if eval_btn:
    if model_answer and student_answer:

        m = preprocess(model_answer)
        s = preprocess(student_answer)

        sim = similarity(m, s)
        key, common = keyword_match(m, s)
        length = length_score(m, s)

        final = (sim*w1 + key*w2 + length*w3)
        marks = round(final * max_marks, 2)

        # Feedback
        if marks > 0.75 * max_marks:
            feedback = "🌟 Excellent"
        elif marks > 0.5 * max_marks:
            feedback = "👍 Good"
        elif marks > 0.3 * max_marks:
            feedback = "⚠️ Average"
        else:
            feedback = "❌ Poor"

        st.subheader("📊 Results")

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Marks", f"{marks}/{max_marks}")
        c2.metric("Similarity", round(sim, 2))
        c3.metric("Keyword Match", round(key, 2))
        c4.metric("Length Score", round(length, 2))

        st.progress(int((marks/max_marks)*100))

        st.markdown("### 🧠 Feedback")
        st.info(feedback)

        # Save for later use
        st.session_state['keywords'] = common

        # Download
        result = f"Marks: {marks}\nSimilarity: {sim}\nKeyword: {key}\nLength: {length}\nFeedback: {feedback}"
        st.download_button("⬇️ Download Result", result)

    else:
        st.warning("Enter both answers!")

# ------------------ KEYWORDS ------------------
if show_keywords_btn:
    if 'keywords' in st.session_state:
        st.write("### 🔑 Matched Keywords")
        st.success(", ".join(st.session_state['keywords']))
    else:
        st.warning("Run evaluation first!")

# ------------------ FOOTER ------------------
st.markdown("<center>Made with ❤️ | AI NLP Project | 2026</center>", unsafe_allow_html=True)



