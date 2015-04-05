def contains_digit(number, digit):
    number_str = str(number)
    digit_str = str(digit)
    if digit_str in number_str:
        return True
    else:
        return False


def contains_digits(number, digits):
    count = 0
    for digit in digits:
        if contains_digit(number, digit) == True:
            count += 1
    if count == len(digits):
        return True
    return False


print(contains_digits(402123, [0, 3, 4, 9]))
