# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()

noise_list = [",", ".", ";", ":", "?", "’", "/", "'", "\"", "\\", "{", "}",
				"|", "[", "]", "(", ")", "*", "+", "=", "-", "_", "^",
				"%", "#", "!", "`", "~", "<", ">"]
def normalize(filename):
	fo = open(filename, "r")
	text = fo.read()
	text = text.lower()

	noise_free_list = [char for char in text if char not in noise_list]
	noise_free_text = "".join(noise_free_list)
	words = noise_free_text.split()
	
	lemmatized = ""
	for word in words:
		lemmatized += ' ' + lem.lemmatize(word, "v")
	fo.close()
	return lemmatized

def main():
	#filename = raw_input("Enter input filename > ")
	fo = open("output.txt", "w")
	normalized_text = normalize("sample.txt")
	fo.write(normalized_text)
	fo.close()

main()