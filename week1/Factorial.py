def factorial(n):
	result = 1
	if n == 0 or n == 1:
		return 1
	else:
		while n > 1:
			return n*(factorial(n - 1))

print factorial(1)