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

def prime_divisors(m):
    list1 = []
    for i in range(1, m + 1):
        if m % i == 0 and is_prime(i):
            list1.append(i)
    return list1

def count(z):
    count = 0
    temp = z
    result_count = []
    for i in range(0, len(prime_divisors(z))):
        while temp % prime_divisors(z)[i] == 0:
            count += 1
            temp /= prime_divisors(z)[i]
            f = temp
        temp = f
        result_count.append(count)
        count = 0
    return result_count

def prime_factorization(p):

    result_END = []
    new = 1
    i1 = 0
    for num in range(0, len(prime_divisors(p))):

        if new != p:
            new *= prime_divisors(p)[num] ** count(p)[i1]
            t = prime_divisors(p)[num], count(p)[i1]
            result_END.append(t)
            i1 += 1


    return result_END

print prime_factorization(10952)

