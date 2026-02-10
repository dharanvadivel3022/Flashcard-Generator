# main.py

from utils.text_input import extract_text
from nlp.preprocessing import clean_text, preprocess_text
from nlp.summarizer import generate_summary
from nlp.question_generator import generate_flashcards
from ocr.ocr_engine import extract_text_from_image
from adaptive.adaptive_engine import AdaptiveEngine
from tts.text_to_speech import read_flashcard


def main():
    print("=== AI Flashcard Generator ===")

    # ---------- STEP 1: TEXT INPUT ----------
    file_path = "sample_text.pdf"  # or sample_input.txt
    raw_text = extract_text(file_path)

    print("\n--- Extracted Text ---")
    print(raw_text[:500])

    # ---------- STEP 2: NLP PREPROCESSING ----------
    cleaned = clean_text(raw_text)
    processed = preprocess_text(cleaned)

    # ---------- STEP 3: SUMMARIZATION ----------
    summary = generate_summary(processed)

    print("\n--- Summary ---")
    print(summary)

    # ---------- STEP 4: FLASHCARD GENERATION ----------
    flashcards = generate_flashcards(summary)

    print("\n--- Flashcards ---")
    for i, card in enumerate(flashcards, 1):
        print(f"\nFlashcard {i}")
        print("Q:", card["question"])
        print("A:", card["answer"])

    # ---------- STEP 5: OCR (OPTIONAL) ----------
    print("\n--- OCR Output ---")
    ocr_text = extract_text_from_image("notes.jpg")
    print(ocr_text[:300])

    # ---------- STEP 6: ADAPTIVE LEARNING ----------
    adaptive_engine = AdaptiveEngine()
    adaptive_engine.record_attempt("card1", True)
    print("\nDue cards:", adaptive_engine.get_due_cards())

    # ---------- STEP 7: TEXT TO SPEECH ----------
    if flashcards:
        read_flashcard(
            flashcards[0]["question"],
            flashcards[0]["answer"]
        )


if __name__ == "__main__":
    main()
