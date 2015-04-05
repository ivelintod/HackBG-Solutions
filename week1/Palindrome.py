def palindrome(obj):
	temp = str(obj)
	length = len(temp)
	end_index = length - 1
	start_index = 0
	for items in temp:
		if temp[start_index] == temp[end_index]:
			start_index += 1
			end_index -= 1
			return True
		else:
			return False

print palindrome("bqlhlqb")
