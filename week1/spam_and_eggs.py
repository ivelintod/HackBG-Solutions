def count_divisions(n):
    count_div = 0
    while n % 3 == 0:
        count_div += 1
        n /= 3
    return count_div

def eggs(n1):
    return count_divisions(n1) * "spam "

def prepare_meal(number):
    if number % 5 == 0:
        if count_divisions(number) == 0:
            return 'eggs'
        else:
            return eggs(number) + 'and eggs'
    else:
        return eggs(number)

print(prepare_meal(6))
