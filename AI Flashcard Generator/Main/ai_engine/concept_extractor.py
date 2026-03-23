import spacy

nlp = spacy.load("en_core_web_sm")


def extract_concepts(text):

    doc = nlp(text)

    concepts = set()

    for chunk in doc.noun_chunks:

        if len(chunk.text.split()) >= 2:
            concepts.add(chunk.text.strip())

    return list(concepts)
