import spacy

nlp = spacy.load('en_core_web_sm')
text = "Steve Jobs was the cofounder of Apple Inc."

doc = nlp(text)
anonymized_text = text

for ent in doc.ents:
    if ent.label_ in ['PERSON', 'ORG', 'GPE']:
        anonymized_text = anonymized_text.replace(ent.text, "[REDACTED]")

print(anonymized_text)