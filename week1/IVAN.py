def is_prime(number):
     divisors = [x for x in range(2, number) if number % x == 0]
     if divisors == []:
        return "Prime"
     else:
        return "Not prime"

print is_prime(18)
