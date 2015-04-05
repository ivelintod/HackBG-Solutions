def sum_of_digits(n):
	import math
	digits = str(n)
	n = math.fabs(n)
	total_sum = 0
	for digit in digits:
		digit_temp = n % 10
		total_sum += digit_temp
		n = n // 10
	return int(total_sum)

print (sum_of_digits(-195))

