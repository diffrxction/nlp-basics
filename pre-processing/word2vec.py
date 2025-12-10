from gensim.models import Word2Vec
import nltk
from nltk.corpus import stopwords

text = "The horse is galloping on the field."
text1 = "The cat is lying down on the mat."

def filter_text(text):
    words = text.split()
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [word for word in words if word not in stop_words]
    return filtered_sentence

texts = []
texts.append(text)
texts.append(text1)

tokens = list(filter_text(text) for text in texts)

model = Word2Vec(tokens, vector_size=10, window=5, min_count=1, workers=4)
vector = model.wv['cat']

print(vector)