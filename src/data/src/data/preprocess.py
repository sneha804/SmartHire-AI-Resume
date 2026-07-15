import re
import string
import pandas as pd
import nltk

from nltk.corpus import stopwords

nltk.download("stopwords")

STOP_WORDS = set(stopwords.words("english"))


def clean_text(text):
    """Clean and normalize text."""

    if pd.isna(text):
        return ""

    text = str(text).lower()

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)

    text = re.sub(r"\S+@\S+", "", text)

    text = re.sub(r"\d+", " ", text)

    text = text.translate(str.maketrans("", "", string.punctuation))

    words = [
        word
        for word in text.split()
        if word not in STOP_WORDS
    ]

    return " ".join(words)
