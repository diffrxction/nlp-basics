from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "The horse scared the cat.",
    "The cat scared the dog.",
    "The dog scared the child.",
    "The child chased the cat."
]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print(tfidf_matrix)
print(tfidf_matrix.toarray())