from sklearn.datasets import fetch_20newsgroups

def load_data():
    return fetch_20newsgroups(
        subset="all",
        remove=("headers", "footers", "quotes"),
        download_if_missing=False
    ).data, fetch_20newsgroups(
        subset="all",
        remove=("headers", "footers", "quotes"),
        download_if_missing=False
    ).target
