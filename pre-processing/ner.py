import nltk

# nltk.download('popular')
# nltk.download('words')

text = "Steve Jobs' horse is galloping on the field inside Apple Inc. premises."
tokens = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)
named_entities = nltk.ne_chunk(pos_tags)

print(named_entities)