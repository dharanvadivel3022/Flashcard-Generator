"""
NLP Preprocessing Module
------------------------
Cleans and prepares raw text for summarization and question generation
"""

import re
import spacy
import nltk
from nltk.corpus import stopwords
try:
    stop_words = set(stopwords.words("english"))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words("english"))




nlp = spacy.load("en_core_web_sm")


def clean_text(text):
    """
    Removes special characters and extra spaces
    """
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9.,? ]', '', text)
    return text.strip()


def preprocess_text(text):
    """
    Tokenizes, removes stopwords, and lemmatizes text
    """
    doc = nlp(text)
    processed_tokens = []

    for token in doc:
        if token.text.lower() not in stop_words and not token.is_punct:
            processed_tokens.append(token.lemma_)

    return " ".join(processed_tokens)
