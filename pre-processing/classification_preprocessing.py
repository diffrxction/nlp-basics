from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

documents = [
    "The horse scared the cat.",
    "The cat scared the dog.",
    "The dog scared the child.",
    "The child loved the cat."
]

labels = [1, 1, 1, 0]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

print(X_train.shape, len(y_train))
print(X_test)