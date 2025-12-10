import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
text = "The horse is galloping on the field."
words = text.split()
stop_words = set(stopwords.words('english'))
filtered_sentence = [w for w in words if not w in stop_words]

print(filtered_sentence)