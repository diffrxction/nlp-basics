from gensim.models.doc2vec import Doc2Vec, TaggedDocument

documents = [
    "The horse scared the cat.",
    "The cat scared the dog.",
    "The dog scared the child.",
    "The child chased the cat."
]

tagged_data = [TaggedDocument(words=doc.split(), tags=[str(i)]) for i, doc in enumerate(documents)]
model = Doc2Vec(tagged_data, vector_size=50, window=2, min_count=1, epochs=100)
doc_vector = model.infer_vector("Dogs are scared of cats.".split())
print(doc_vector)