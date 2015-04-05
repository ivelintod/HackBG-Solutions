def is_number_balanced(n):
    str_n = str(n)
    half_length = len(str_n) // 2
    first_half = str_n[0:half_length]
    if len(str_n) % 2 == 0:
        second_half = str_n[half_length:len(str_n)]
    else:
        second_half = str_n[half_length + 1:len(str_n)]
    sum1 = 0
    sum2 = 0
    for i in first_half:
        sum1 += int(i)
    for i2 in second_half:
        sum2 += int(i2)
    if sum1 == sum2:
        return True
    else:
        return False

print(is_number_balanced(1238033))
