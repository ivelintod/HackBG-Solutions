def sum_matrix(m):
    result = 0
    for i in m:
        for i1 in i:
            result += i1
    return result

print sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
