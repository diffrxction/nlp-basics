from transformers import XLMRobertaTokenizer, XLMRobertaModel

tokenizer = XLMRobertaTokenizer.from_pretrained('xlm-roberta-base')
model = XLMRobertaModel.from_pretrained('xlm-roberta-base')

text = "Bonjour tout le monde"
inputs = tokenizer(text, return_tensors='pt')
outputs = model(**inputs)