def zero_insert(n):
    str_n = str(n)
    length = len(str_n)
    result = ""
    if n == 1:
        return 1

    for index in range(0, length - 1):
        if str_n[index] == str_n[index + 1] or (int(str_n[index]) + int(str_n[index + 1])) % 10 == 0:
            result += str_n[index] + str(0)
        else:
            result += str_n[index]
    result = result + str_n[length - 1]
    return result

print zero_insert(55555555555)

