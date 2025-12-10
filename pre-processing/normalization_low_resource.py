from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

text = "Example sentence in low-resource language."
inputs = tokenizer(text, return_tensors='pt')

outputs = model(**inputs)