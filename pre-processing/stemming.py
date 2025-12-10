import nltk
from nltk.stem import PorterStemmer, SnowballStemmer

stemmer = SnowballStemmer('english')
words = ["galloping", "gallop", "run", "ran", "horse", "field"]
stemmed_words = [stemmer.stem(word) for word in words]
# this changes horse to hors as per stemmer behavior, same for PorterStemmer
print(stemmed_words)