def hack(n):
    binary_n = bin(n)[2:]
    one_count = binary_n.count('1')
    if binary_n == binary_n[::-1] and one_count % 2 != 0:
        return True
    else:
        return False

def next_hack(n1):
    for i in range(n1 + 1, 100000000):
        if hack(i):
            return i
            break

print next_hack(8031)

