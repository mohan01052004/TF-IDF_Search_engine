from src.evaluation import precision, recall

def test_precision_recall():
    relevant = {1, 2}
    retrieved = {2, 3}
    assert precision(relevant, retrieved) == 0.5
    assert recall(relevant, retrieved) == 0.5
