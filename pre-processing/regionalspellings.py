british_to_american = {
    "colour": "color",
    "favourite": "favorite",
}

def normalize_dialect(text):
    words = text.split()
    normalized_words = [british_to_american.get(word, word) for word in words]
    return " ".join(normalized_words)

text = "My favourite colour is golden."

print(normalize_dialect(text))