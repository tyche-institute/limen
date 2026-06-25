# lang_detection.py
import langdetect
from translation_confidence import assess_confidence


def detect_language(text):
    """
    Detects the language of a given text using langdetect.
    
    Args:
        text (str): Input text to detect language.
    
    Returns:
        str: Detected language code (e.g., 'et' for Estonian).
    """
    try:
        return langdetect.detect(text)
    except:
        return 'unknown'


def assess_translation_confidence(source_text, translation):
    """
    Evaluates confidence in machine-translated text.
    
    Args:
        source_text (str): Original text in source language.
        translation (str): Translated text.
    
    Returns:
        dict: Confidence score (0-1) and language detection confidence.
    """
    lang = detect_language(source_text)
    return {
        'source_language': lang,
        'confidence': assess_confidence(source_text, translation, lang)
    }
