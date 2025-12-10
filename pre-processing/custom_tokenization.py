from tokenizers import BertWordPieceTokenizer

tokenizer = BertWordPieceTokenizer()
tokenizer.train(["data/corpus.txt"], vocab_size=30000, min_frequency=2)

encoding = tokenizer.encode("Natural Language Processing!")
print(encoding.tokens)