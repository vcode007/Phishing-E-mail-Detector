import re

def clean_email(text):
    text = re.sub(r"http\S+", "", text)         # remove links
    text = re.sub(r"\S+@\S+", "", text)          # remove email addresses
    text = re.sub(r"[^\w\s]", "", text)          # remove punctuation
    text = text.lower().strip()
    return text
