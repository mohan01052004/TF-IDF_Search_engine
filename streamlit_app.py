import streamlit as st

# ---------- IMPORTS ----------
from src.load_data import load_data
from src.preprocess import preprocess
from src.tfidf import build_tfidf
from src.search import search


# ---------- PAGE CONFIG (TOP) ----------
st.set_page_config(
    page_title="TF-IDF Search Engine",
    layout="wide"
)

st.title("🔍 TF-IDF Search Engine")
st.write("Search across the 20 Newsgroups dataset")


# ---------- CACHED ENGINE (ADD HERE) ----------
@st.cache_resource
def load_engine():
    docs, labels = load_data()
    docs_tokens = [preprocess(d) for d in docs]
    vectorizer, tfidf_matrix = build_tfidf(docs_tokens)
    return docs, vectorizer, tfidf_matrix


# ---------- LOAD ENGINE (CALL HERE) ----------
with st.spinner("Building TF-IDF index... Please wait ⏳"):
    docs, vectorizer, tfidf_matrix = load_engine()


# ---------- SEARCH UI ----------
query = st.text_input("Enter your search query")

if query:
    q_tokens = preprocess(query)
    doc_ids, scores = search(q_tokens, vectorizer, tfidf_matrix)

    st.subheader("Top Results")
    for i, doc_id in enumerate(doc_ids[:10], start=1):
        st.markdown(f"### Rank {i}")
        st.write(f"**Score:** {scores[i-1]:.4f}")
        st.write(docs[doc_id][:300])
        st.divider()
