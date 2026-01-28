# src/preprocess.py

import nltk
import re
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    tokens = nltk.word_tokenize(re.sub(r'[^a-zA-Z]', ' ', text))
    tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 2]
    return tokens
