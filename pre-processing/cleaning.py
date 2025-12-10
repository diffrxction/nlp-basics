import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text) # digits
    text = re.sub(r'[^\w\s]', '', text) # punctuation removed
    text = re.sub(r'\s+', ' ', text).strip() # extra spaces
    return text

sample_text = "Hello, World!     2025."
print(preprocess_text(sample_text))