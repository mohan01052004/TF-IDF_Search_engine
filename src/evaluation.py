# src/evaluation.py

def precision(relevant, retrieved):
    return len(relevant & retrieved) / len(retrieved)

def recall(relevant, retrieved):
    return len(relevant & retrieved) / len(relevant)
