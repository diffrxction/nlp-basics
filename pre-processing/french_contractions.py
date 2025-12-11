import re

def expand_french_contractions(text):
    text = re.sub(r"\bl'", "le ", text)
    return text

text = "l'amour est beau"
print(expand_french_contractions(text))