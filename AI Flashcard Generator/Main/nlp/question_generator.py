import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")


def extract_keywords(doc, top_n=10):

    keywords = []

    for token in doc:

        if (
            token.pos_ in ["NOUN", "PROPN"]
            and not token.is_stop
            and len(token.text) > 2
        ):
            keywords.append(token.lemma_.lower())

    keyword_freq = Counter(keywords)

    return [word for word, _ in keyword_freq.most_common(top_n)]


def generate_flashcards(text):

    doc = nlp(text)

    sentences = [sent.text.strip() for sent in doc.sents]

    keywords = extract_keywords(doc)

    flashcards = []
    used_sentences = set()

    for keyword in keywords:

        for sentence in sentences:

            if keyword.lower() in sentence.lower():

                if sentence not in used_sentences:

                    question = f"What is {keyword.title()}?"

                    answer = sentence

                    flashcards.append({
                        "question": question,
                        "answer": answer
                    })

                    used_sentences.add(sentence)

                    break

    return flashcards
