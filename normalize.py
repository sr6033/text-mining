from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer
stem = PorterStemmer()

word = "multiplying"
word = lem.lemmatize(word, "v")
print(word)

word = "multiplying"
word = stem.stem(word)
print(word)