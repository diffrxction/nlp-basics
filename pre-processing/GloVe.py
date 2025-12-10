import numpy as np

def load_glove_embeddings(filepath):
    embeddings = {}
    with open(filepath, 'r') as f:
        for line in f:
            values = f.split()
            word = values[0]
            vector = np.asarray(values[1:], dtype='float32')
            embeddings[word] = vector

    return embeddings

embeddings_index = load_glove_embeddings('glove.6B.100d.txt')
print(embeddings_index['cat'])
