from nltk.corpus import stopwords
from gensim.models import FastText

documents = [
    "The horse scared the cat.",
    "The cat scared the dog.",
    "The dog scared the child.",
    "The child chased the cat."
]

def process(sentence):
    words = sentence.split()
    stop_words = set(stopwords.words('english'))
    # filtered_sentence = [word for word in words if word not in stop_words]
    return words

tokens = list(process(sentence) for sentence in documents)

model = FastText(documents, vector_size=100, window=5, min_count=1, workers=4)
vector = model.wv['cat']
print(vector)