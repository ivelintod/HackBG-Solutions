def fib_number(n):
	count = 2
	temp = 0
	result = [1]
	concat = ""
	if n == 1:
		return 1
	elif n == 2:
		return 11
	else:
		result.append(1)
		while count < n:
			temp_fact = result[count - 2] + result[count - 1]
			result.append(temp_fact)
			count += 1
		result = [str(i) for i in result]
		for i in result:
			concat += result[temp]
			temp += 1
		return concat
print fib_number(10)

