from nltk import ngrams

text = "The horse is galloping on the field."
n = 2
bigrams = ngrams(text.split(), n=n) # split() to break into sentence
print(list(bigrams))