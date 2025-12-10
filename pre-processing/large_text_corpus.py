from gensim.models import Word2Vec

def generate_batches(corpus, batch_size):
    for i in range(0, len(corpus), batch_size):
        yield corpus[i: i + batch_size]

model = Word2Vec(vector_size=100, window=5, min_count=1)
large_corpus = "Large body of text."
for batch in generate_batches(large_corpus, batch_size=1000):
    model.build_vocab(batch, update=True)
    model.train(batch, total_examples=len(batch), epochs=model.epochs)
