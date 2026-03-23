import spacy

from ai_engine.concept_extractor import extract_concepts
from ai_engine.semantic_ranker import rank_concepts
from ai_engine.question_generator import generate_questions


nlp = spacy.load("en_core_web_sm")


def generate_flashcards(text):

    doc = nlp(text)

    sentences = [sent.text.strip() for sent in doc.sents]

    concepts = extract_concepts(text)

    ranked = rank_concepts(text, concepts)

    flashcards = generate_questions(ranked, sentences)

    return flashcards[:50]
