from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "The horse scared the cat.",
    "The cat scared the dog.",
    "The dog scared the child.",
    "The child chased the cat."
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

lda = LatentDirichletAllocation(n_components=2, random_state=42)
lda.fit(X)

terms = vectorizer.get_feature_names_out()
for idx, topic in enumerate(lda.components_):
    print(f"Topic {idx}:")
    print(' '.join([terms[i] for i in topic.argsort()[-5:]]))
