# utils/text_input.py

"""
Text Input Module
-----------------
This module handles input from:
1. Plain text files (.txt)
2. PDF documents (.pdf)

Output:
- Extracted raw text as a string
"""

import os
from PyPDF2 import PdfReader


def read_text_file(file_path):
    """
    Reads text from a .txt file.

    Parameters:
        file_path (str): Path to the text file

    Returns:
        str: Extracted text
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as e:
        print("Error reading text file:", e)
        return ""


def read_pdf_file(file_path):
    """
    Extracts text from a PDF file.

    Parameters:
        file_path (str): Path to the PDF file

    Returns:
        str: Extracted text from all pages
    """
    extracted_text = ""

    try:
        reader = PdfReader(file_path)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text + "\n"

        return extracted_text

    except Exception as e:
        print("Error reading PDF file:", e)
        return ""


def extract_text(file_path):
    """
    Determines file type and extracts text accordingly.

    Parameters:
        file_path (str): Path to input file

    Returns:
        str: Extracted raw text
    """
    if not os.path.exists(file_path):
        print("File does not exist.")
        return ""

    _, extension = os.path.splitext(file_path)

    if extension.lower() == ".txt":
        return read_text_file(file_path)

    elif extension.lower() == ".pdf":
        return read_pdf_file(file_path)

    else:
        print("Unsupported file format.")
        return ""
