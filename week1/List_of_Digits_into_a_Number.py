def to_number(digits):
	result = 0
	length = len(digits)
	temp = 1
	for i in digits:
		while length > 0:
			f = digits[length - 1] * temp
			length -= 1
			temp *= 10
			result += f
	return result 

print (to_number([1,2,3,5,6]))
print (to_number([9,9,9]))