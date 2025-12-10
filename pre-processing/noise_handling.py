from textblob import TextBlob

text = "The hrse is glloping on the feild."
blob = TextBlob(text)
corrected_text = str(blob.correct())
print(corrected_text)