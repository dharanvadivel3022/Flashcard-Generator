from nlp.summarizer import generate_summary

text = """
Artificial Intelligence is transforming many industries.
It enables machines to learn from data and perform tasks that normally require human intelligence.
AI is widely used in healthcare, finance, transportation, and education.
Machine learning is a subset of AI that focuses on learning patterns from data.
"""

summary = generate_summary(text)

print("SUMMARY:")
print(summary)
