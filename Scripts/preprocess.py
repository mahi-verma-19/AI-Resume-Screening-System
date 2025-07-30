import spacy
import re

# Load spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Function to clean the text
def clean_text(text):
    text = text.lower()                          # Convert to lowercase
    text = re.sub(r'\s+', ' ', text)             # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)          # Remove punctuation
    return text

# Function to preprocess using spaCy
def preprocess(text):
    text = clean_text(text)
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)
