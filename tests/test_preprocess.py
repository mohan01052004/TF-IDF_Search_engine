from src.preprocess import preprocess

def test_preprocess_removes_stopwords():
    tokens = preprocess("This is a sample TEXT.")
    assert "this" not in tokens
