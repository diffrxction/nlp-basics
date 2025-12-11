import numpy as np
from collections import Counter
from imblearn.over_sampling import RandomOverSampler, SMOTE
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

texts = [
    "The horse scared the cat.",
    "The cat scared the dog.",
    "The dog scared the child.",
    "The child loves the cat."
]

labels = np.array([1, 1, 1, 0])

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

tfvectorizer = TfidfVectorizer()
Xtf = tfvectorizer.fit_transform(texts)

counts = Counter(labels)

min_count = min(counts.values())

if min_count <= 1:
    ros = RandomOverSampler(random_state=42)
    X_res, y_res = ros.fit_resample(X, labels)

else:
    k = min(5, min_count - 1)

    smote = SMOTE(random_state=42, k_neighbors=k)
    X_res, y_res = smote.fit_resample(Xtf.toarray(), labels)

print(y_res)
