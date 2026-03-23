from utils.text_input import extract_text
from nlp.preprocessing import clean_text
from nlp.summarizer import generate_summary
# from nlp.question_generator import generate_flashcards
from adaptive.adaptive_engine import AdaptiveEngine
from tts.text_to_speech import read_flashcard
from ai_engine.pipeline import generate_flashcards




def main():

    print("=== AI Flashcard Generator ===")

    # STEP 1: INPUT
    file_path = "Types Of Attacks Chapter 2.pdf"
    raw_text = extract_text(file_path)

    if not raw_text:
        print("No text extracted.")
        return

    print("\n--- Extracted Text ---")
    print(raw_text[:200000])

    # STEP 2: CLEANING
    cleaned_text = clean_text(raw_text)

    # STEP 3: SUMMARIZATION
    summary = generate_summary(cleaned_text)

    print("\n--- Summary ---")
    print(summary)

    # STEP 4: FLASHCARD GENERATION
    # flashcards = generate_flashcards(cleaned_text)
    flashcards = generate_flashcards(cleaned_text)

    if not flashcards:
        print("\nNo flashcards generated.")
        return

    print("\n----- FLASHCARDS -----")

    for i, card in enumerate(flashcards, 1):
        print(f"\nFlashcard {i}")
        print("Q:", card["question"])
        print("A:", card["answer"])

    # STEP 5: ADAPTIVE ENGINE
    engine = AdaptiveEngine()
    engine.record_attempt("card1", True)
    print("\nDue cards:", engine.get_due_cards())

    # STEP 6: TEXT TO SPEECH
    read_flashcard(
        flashcards[0]["question"],
        flashcards[0]["answer"]
    )


if __name__ == "__main__":
    main()
