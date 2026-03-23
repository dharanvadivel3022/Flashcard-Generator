from collections import Counter
import spacy

nlp = spacy.load("en_core_web_sm")


def rank_concepts(text, concepts):

    doc = nlp(text)

    freq = Counter()

    for token in doc:

        if token.text in concepts:
            freq[token.text] += 1

    ranked = sorted(concepts, key=lambda x: freq[x], reverse=True)

    return ranked
