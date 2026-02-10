import spacy

nlp = spacy.load("en_core_web_sm")


def generate_flashcards(text, max_cards=5):
    doc = nlp(text)
    flashcards = []

    for sent in doc.sents:
        if len(sent.text) < 40:
            continue

        subject = None
        for token in sent:
            if token.dep_ in ("nsubj", "nsubjpass"):
                subject = token.text
                break

        if subject:
            question = f"What is {subject}?"
            flashcards.append({
                "question": question,
                "answer": sent.text.strip()
            })

        if len(flashcards) >= max_cards:
            break

    return flashcards
