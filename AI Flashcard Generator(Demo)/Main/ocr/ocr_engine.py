"""
OCR Module
----------
Extracts text from image files using Tesseract OCR
"""

import pytesseract
from PIL import Image
import cv2
import os

# OPTIONAL: set tesseract path if not in PATH
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_path):
    """
    Improves image quality for better OCR accuracy
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blur, 0, 255,
                            cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return thresh

def extract_text_from_image(image_path):
    """
    Extracts text from image using OCR
    """
    if not os.path.exists(image_path):
        return ""

    processed_img = preprocess_image(image_path)
    text = pytesseract.image_to_string(processed_img)
    return text
