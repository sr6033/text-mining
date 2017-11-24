#!/usr/bin/python
# Naive approach of noise removal
noise_list = ["is", "a", "this", "...", "an", "the", "of", "for", ".", ",", "'", "{", "}"
				"[", "]", "(", ")", "\\", "/", "!", "`", "*", "are", "were", "was", 
				"am", "have", "has", "to", "be", "from" "had", "do", "does", "did", "done"]
def _remove_noise(filename):
	fo = open(filename, "r")
	text = fo.read()
	text = text.lower()
	words = text.split()
	noise_free_words = [word for word in words if word not in noise_list]
	noise_free_text = " ".join(noise_free_words)
	return noise_free_text

def main():
	filename = raw_input("Enter input filename > ")
	print(_remove_noise(filename))

main()