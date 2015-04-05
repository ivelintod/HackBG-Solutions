def to_digits(n):
	list_of_digits = []
	digits = str(n)
	for digit in digits:
		digit = n % 10
		list_of_digits.append(digit)
		n = n // 10
	return list_of_digits[::-1]

print (to_digits(45556))