def bombs_away(n):
    target = ""
    count = 0
    for i in range(0, length):
        length1 = len(m[i])
        temp += length1
    row_length = temp / length

    for rows in range(0, len(m)):
        for i in range(0, row_length):
            matrix = n[rows][i]
            matrix_new = n[rows][i]
            if matrix > 0:
                damage = matrix[[]]




def matrix_bombing_plan(m):
    length = len(m)
    temp = 0
    for i in range(0, length):
        length1 = len(m[i])
        temp += length1
    row_length = temp / length

    bomb_dict = {(row, i):0 for row in range(0, length) for i in range(0, row_length)}
    '''target = 0
    list1 = []
    for row in m:
        for i in range(0, len(row)):
            target = row[i]
            list1.append(target)

    index = 0
    for key in bomb_dict:
        bomb_dict[key] = list1[index]
        index += 1'''






    return bomb_dict

print matrix_bombing_plan([[10, 10, 10],
                           [10, 9, 10],
                           [10, 10, 10]])
