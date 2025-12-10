from imblearn.over_sampling import RandomOverSampler
from sklearn.feature_extraction.text import CountVectorizer

texts = [
    "The horse scared the cat.",
    "The cat scared the dog.",
    "The dog scared the child.",
    "The child loves the cat."
]

labels = [1, 1, 1, 0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
ros = RandomOverSampler(random_state=42)
X_res, y_res = ros.fit_resample(X, labels)
print(y_res)
