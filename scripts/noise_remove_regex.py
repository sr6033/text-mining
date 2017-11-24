# Noise removal using regular expressions

import re

def _remove_regex(input_text, regex_pattern):
	urls = re.finditer(regex_pattern, input_text) # Check
	for i in urls:
		input_text = re.sub(i.group().strip(), '', input_text) # Check
	return input_text

regex_pattern = "#[\w]*"

print(_remove_regex("remove this #hastag from the line.", regex_pattern))