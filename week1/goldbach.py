def is_prime(n):
    if n == 1 or n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True


def prime_until_n(n):
    res = []
    for i in range(2, n + 1):
        if is_prime(i):
            res.append(i)
    return res


def goldbach(n):
    combination = prime_until_n(n)
    length = len(combination)
    res = []
    for i in range(length):
        for j in range(length):
            if (int(combination[i]) + int(combination[j])) == n:
                comb_t = (int(combination[i]), int(combination[j]))
                res.append(comb_t)
    length = len(res)
    half = length / 2
    if length % 2 == 0:
        return res[: half]
    else:
        return res[: (half + 1)]

print goldbach(10)
