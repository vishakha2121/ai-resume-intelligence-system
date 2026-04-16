import re

def clean_text(text):
    # Remove extra spaces, newlines, special chars
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s\.\,\-\:\;]', '', text)
    return text.strip()