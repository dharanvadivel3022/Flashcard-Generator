def generate_questions(concepts, sentences):

    flashcards = []

    for concept in concepts:

        for sentence in sentences:

            if concept.lower() in sentence.lower():

                flashcards.append({

                    "question": f"What is {concept}?",
                    "answer": sentence
                })

                break

    return flashcards
