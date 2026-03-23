"""
Text-to-Speech Module
---------------------
Reads questions and answers aloud
"""

import pyttsx3

engine = pyttsx3.init()

def speak_text(text):
    """
    Converts text to speech
    """
    engine.say(text)
    engine.runAndWait()

def read_flashcard(question, answer):
    """
    Reads a flashcard aloud
    """
    speak_text("Question")
    speak_text(question)
    speak_text("Answer")
    speak_text(answer)
