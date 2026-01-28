# src/tfidf.py

from sklearn.feature_extraction.text import TfidfVectorizer

def build_tfidf(docs):
    vectorizer = TfidfVectorizer(tokenizer=lambda txt: txt,
                                 preprocessor=lambda txt: txt,
                                 token_pattern=None,
                                 lowercase=False)
    tfidf_matrix = vectorizer.fit_transform(docs)
    return vectorizer, tfidf_matrix
