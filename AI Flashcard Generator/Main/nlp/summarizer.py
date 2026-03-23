import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict

stop_words = set(stopwords.words("english"))


def generate_summary(text, max_sentences=5):

    sentences = sent_tokenize(text)

    if len(sentences) <= max_sentences:
        return text

    word_freq = defaultdict(int)

    for word in word_tokenize(text.lower()):
        if word.isalnum() and word not in stop_words:
            word_freq[word] += 1

    sentence_scores = {}

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_freq[word]

    ranked = sorted(sentence_scores, key=sentence_scores.get, reverse=True)

    selected = ranked[:max_sentences]

    # preserve original order
    selected.sort(key=lambda s: sentences.index(s))

    return " ".join(selected)
