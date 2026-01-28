from src.search import search
from src.tfidf import build_tfidf

docs = [["test", "document"], ["another", "test"]]
vec, mat = build_tfidf(docs)

def test_search_returns_results():
    ids, _ = search(["test"], vec, mat)
    assert len(ids) > 0
