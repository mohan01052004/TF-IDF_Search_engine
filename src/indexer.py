# src/indexer.py

from collections import defaultdict

def build_inverted_index(docs_tokens):
    inv_index = defaultdict(set)
    for doc_id, tokens in enumerate(docs_tokens):
        for token in tokens:
            inv_index[token].add(doc_id)
    return inv_index
