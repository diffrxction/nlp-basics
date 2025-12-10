import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
words = ["galloping", "gallop", "run", "ran", "horses", "field"]
# lemmatized_words = [lemmatizer.lemmatize(word, pos='n') for word in words]
lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]

print(lemmatized_words)