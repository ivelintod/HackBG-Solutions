def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		while n > 1:
			return n * factorial(n-1) 
def fact_digits(n):
	total_sum = 0
	digits = str(n)
	for digit in digits:
		digit = n % 10
		total_sum += factorial(digit)
		n = n // 10
	return total_sum

print fact_digits(43)