def contains_digit(number, digit):
    number_str = str(number)
    digit_str = str(digit)
    if digit_str in number_str:
        return True
    else:
        return False

print(contains_digit(12346789, 5))
