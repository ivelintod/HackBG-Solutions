def char_histogram(string):
	dict = {}
	count = 0
	for i in string:
		dict[i] = count
	for key in dict:
		key_occurance = string.count(key)
		dict[key] = key_occurance
		
		
	return dict

print char_histogram("Hello")
print char_histogram("AAAaaa")