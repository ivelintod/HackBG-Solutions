def magic_square(matrix):

    row_len = len(matrix[0])
    sum_temp_col = 0
    sum_temp_row = 0
    sum_temp_main_diag = 0
    sum_temp_sec_diag = 0
    sums = []
    for i in range(row_len):
        for row in matrix:
            sum_temp_col += row[i]
        sums.append(sum_temp_col)
        sum_temp_col = 0
    for row in matrix:
        for i in range(row_len):
            sum_temp_row += row[i]
        sums.append(sum_temp_row)
        sum_temp_row = 0
    j = 0
    for row in matrix:
        sum_temp_main_diag += row[j]
        j += 1
    sums.append(sum_temp_main_diag)

    f = row_len - 1
    for row in matrix:
        sum_temp_sec_diag += row[f]
        f -= 1
    sums.append(sum_temp_sec_diag)

    for item in range(len(sums) - 1):
        if sums[item] == sums[item + 1]:
            return True
        else:
            return False


print magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]])


