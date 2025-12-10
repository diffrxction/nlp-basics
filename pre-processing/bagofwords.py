from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "The horse scared the cat.",
    "The cat scared the dog.",
    "The dog scared the child.",
    "The child chased the cat."
]

vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(documents)

print(bow_matrix)