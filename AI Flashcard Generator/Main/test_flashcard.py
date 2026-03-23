from nlp.question_generator import generate_flashcards

text = """
Artificial Intelligence (AI) is a branch of computer science that focuses on creating intelligent
machines capable of performing tasks that typically require human intelligence. These tasks include
learning, reasoning, problem-solving, understanding natural language, and perception. Machine
Learning is a subset of AI that allows systems to learn from data without being explicitly
programmed. Deep Learning, a further subset, uses neural networks with multiple layers to analyze
complex patterns in data. AI is widely used in applications such as recommendation systems,
speech recognition, image processing, autonomous vehicles, and healthcare diagnostics. Despite
its advantages, AI also raises ethical concerns related to privacy, bias, and job displacement.
"""

flashcards = generate_flashcards(text)

for i, card in enumerate(flashcards, 1):
    print(f"\nFlashcard {i}")
    print("Q:", card["question"])
    print("A:", card["answer"])
