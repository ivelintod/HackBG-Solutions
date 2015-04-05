def is_increasing(seq):
    length = len(seq)
    for index in range(0, length - 1):
        first_temp = seq[index]
        second_temp = seq[index + 1]
        if first_temp < second_temp:
            result = True
        else:
            result = False
    return result

print is_increasing([1,2,3])



