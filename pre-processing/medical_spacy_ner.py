import scispacy
import spacy
from scispacy.linking import EntityLinker

nlp = spacy.load('en_core_sci_sm')
linker = EntityLinker(name='umls')

text = "Soframycin and Paracetamol are commonly sold OTG medicines in India."
doc = nlp(text)
entities = [(ent.text, ent._.umls_ents) for ent in doc.ents]

print(entities)