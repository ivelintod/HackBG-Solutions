matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

result = [[row[i] for row in matrix] for i in range(0, 4)]

bomb_dict = {(x, y):0 for x in range(0, len(m)) for y in range(0, len(row)) )}
