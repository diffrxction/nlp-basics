from contractions import fix

def preprocess_for_sentiment(text):
    text = fix(text)
    text = text.replace("n't", "not")
    return text

documents = [
    "The horse didn't scare the cat.",
    "The cat scared the dog.",
    "The dog scared the child.",
    "The child chased the cat."
]
# print(list(sentence for sentence in documents))
print(list(preprocess_for_sentiment(sentence) for sentence in documents))