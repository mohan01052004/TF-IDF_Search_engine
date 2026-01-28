from src.indexer import build_inverted_index

def test_inverted_index_simple():
    docs = [["hello", "world"], ["hello"]]
    idx = build_inverted_index(docs)
    assert idx["hello"] == {0, 1}
