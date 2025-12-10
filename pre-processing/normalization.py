import re

def normalize_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text) # URLs removed
    text = re.sub(r'<.*?>', "", text) # HTML removed
    text = re.sub(r'[^\w\s]', '', text) # remove punctuation
    return text

text = "Here's the link to Google.com: https://www.google.com"
print(normalize_text(text))