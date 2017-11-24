# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

'''
doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health."
doc_set = [doc_a, doc_b]
'''
fo = open("data.txt", "r")
text1 = fo.read()
text1 = text1.lower()
text1 = text1.decode('unicode_escape').encode('utf-8')

# compile sample documents into a list
doc_set = [text1]

# Tokenize
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

tokens = []
for i, doc in enumerate(doc_set):
	raw = doc.lower()
	tokens.append(tokenizer.tokenize(raw))

# Remove stop words
from stop_words import get_stop_words
en_stop = get_stop_words('en')

char = ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
		'q','r','s','t','u','v','w','x','y','z', 'thou', 'will', 'shall',
		'come', 'thy']

for i in range(25):
	en_stop.append(char[i])

stopped_tokens = []
for j in tokens:
	stopped_tokens.append([i for i in j if not i in en_stop])

# Normalize
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

texts = []

'''
for j in stopped_tokens:
	s = []
	for i in j:
		i = i.decode('unicode_escape').encode('utf-8')
		str = lem.lemmatize(i, "v")
		s.append(str)

'''

for j in stopped_tokens:
	texts.append(([lem.lemmatize((i.decode('unicode_escape').encode('utf-8')), "v") for i in j]))
#print texts

# Construct Term-Document Matrix
from gensim import corpora, models
dictionary = corpora.Dictionary(texts)

corpus = [dictionary.doc2bow(text) for text in texts]

#print
#print corpus
#print

import gensim

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=20, id2word = dictionary, passes=20)

print(ldamodel.print_topics(num_topics=20, num_words=10))