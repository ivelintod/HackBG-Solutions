def sum_of_divisors(n):
    sum_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors

print sum_of_divisors(1000)
