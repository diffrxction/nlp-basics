import spacy
import wikipediaapi

nlp = spacy.load('en_core_web_sm')
wiki_wiki = wikipediaapi.Wikipedia(user_agent="MyProjectName (merlin@example.com)", language='en')

text = "Apple was founded by Steve Jobs."

doc = nlp(text)
entities = [(ent.text, ent.label_) for ent in doc.ents]

print(entities)

for entity in entities:
    page = wiki_wiki.page(entity[0])
    if page.exists():
        print(f"Entity: {entity[0]}, Wikipedia Link: {page.fullurl}")
