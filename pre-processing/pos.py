import nltk

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = "The horse is galloping on the field."
tokens = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)
print(pos_tags)