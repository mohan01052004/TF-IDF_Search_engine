from sklearn.datasets import fetch_20newsgroups

def load_data():
    dataset = fetch_20newsgroups(
        subset="all",
        remove=("headers", "footers", "quotes"),
        download_if_missing=True
    )
    return dataset.data, dataset.target
