from transformers import pipeline
from utils.preprocess import clean_email

# Load zero-shot classification model
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Labels we want the model to choose from
labels = ["phishing", "legitimate"]

def classify_email(text):
    clean_text = clean_email(text)
    result = classifier(clean_text, candidate_labels=labels)
    prediction = result["labels"][0]
    confidence = result["scores"][0]
    return f"{prediction.upper()} ({confidence:.2f} confidence)"
