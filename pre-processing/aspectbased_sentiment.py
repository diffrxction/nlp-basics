import spacy

nlp = spacy.load('en_core_web_sm')

text = "Steve Jobs was the CEO of Apple Inc., California."
doc = nlp(text)

aspect_terms = [ent.text for ent in doc.ents if ent.label_ in ['PERSON', 'ORG', 'GPE']]
print(aspect_terms)