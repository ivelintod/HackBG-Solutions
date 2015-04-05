def fibonacci(n):
	result = [1]
	result_wrong = []
	count = 2
	if n < 0:
		return result_wrong
	elif n == 0 or n == 1:
		return result
	elif n == 2:
		result.append(1)
		return result
	elif n > 2:
		result.append(1)
		while count < n:
			temp_addition = result[count - 2] + result[count - 1]
			result.append(temp_addition)
			count += 1
		return result

print (fibonacci(10))
	
