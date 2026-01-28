# src/search.py

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def search(query, vectorizer, tfidf_matrix, top_k=10):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    ranked_doc_ids = np.argsort(scores)[::-1][:top_k]
    return ranked_doc_ids, scores[ranked_doc_ids]
