import streamlit as st
import re

from src.load_data import load_data
from src.preprocess import preprocess
from src.tfidf import build_tfidf
from src.search import search


# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="TF-IDF Search Engine", layout="wide")
st.title("🔍 Document Search Engine")
st.write("Search and explore structured articles from the 20 Newsgroups dataset")


# ---------------- SESSION STATE ----------------
if "expanded_doc" not in st.session_state:
    st.session_state.expanded_doc = None


# ---------------- LOAD & CACHE ENGINE ----------------
@st.cache_resource
def load_engine():
    docs, labels = load_data()
    docs_tokens = [preprocess(d) for d in docs]
    vectorizer, tfidf_matrix = build_tfidf(docs_tokens)
    return docs, vectorizer, tfidf_matrix


with st.spinner("Indexing documents... Please wait"):
    docs, vectorizer, tfidf_matrix = load_engine()


# ---------------- SIDEBAR SETTINGS ----------------
st.sidebar.header("Search Settings")
top_k = st.sidebar.slider("Results to show", 5, 20, 10)


# ---------------- SEARCH INPUT ----------------
query = st.text_input("🔎 Search documents")


# ---------------- HELPER FUNCTIONS ----------------
def clean_article(text):
    """Extract structured paragraphs only"""
    return [p.strip() for p in text.split("\n") if len(p.strip()) > 60]


def highlight_keywords(text, query):
    """Highlight query keywords (case-insensitive)"""
    for word in set(query.split()):
        pattern = re.compile(rf"\b({re.escape(word)})\b", re.IGNORECASE)
        text = pattern.sub(r"**\1**", text)
    return text


def get_snippet(text, length=200):
    """Create preview snippet"""
    text = text.replace("\n", " ")
    return text[:length] + "..."


# ---------------- SEARCH RESULTS ----------------
if query:
    q_tokens = preprocess(query)
    doc_ids, scores = search(q_tokens, vectorizer, tfidf_matrix, top_k=top_k)

    st.markdown("## 🔍 Search Results")

    for rank, doc_id in enumerate(doc_ids, start=1):

        snippet = get_snippet(docs[doc_id])

        # ---------- RESULT HEADER ----------
        st.markdown(f"### {rank}. Document {doc_id}")
        st.write(snippet)
        st.caption(f"Relevance score: {scores[rank-1]:.4f}")

        # ---------- TOGGLE BUTTON (YOUR LOGIC) ----------
        label = (
            "⬆️ Collapse article"
            if st.session_state.expanded_doc == doc_id
            else "📄 Read full article"
        )

        if st.button(label, key=f"read_{doc_id}"):
            if st.session_state.expanded_doc == doc_id:
                st.session_state.expanded_doc = None
            else:
                st.session_state.expanded_doc = doc_id

        # ---------- INLINE ARTICLE VIEW ----------
        if st.session_state.expanded_doc == doc_id:
            st.markdown("#### 📄 Full Article")

            paragraphs = clean_article(docs[doc_id])
            for para in paragraphs:
                st.markdown(highlight_keywords(para, query))

        st.divider()
