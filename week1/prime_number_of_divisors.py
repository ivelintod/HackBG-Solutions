def is_prime(n):
	if n == 1:
		return False
	elif n == 2:
		return True
	for i in range(2, n):
		if n % i == 0:
			return False
	else: 
		return True


def prime_numbers_of_divisors(n):
	count_pnd = 0
	for i in range(1, n + 1):
		if n % i == 0:
			count_pnd += 1
		result = count_pnd
	return is_prime(result)
	

print(prime_numbers_of_divisors(5))