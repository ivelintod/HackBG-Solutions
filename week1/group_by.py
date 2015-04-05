def groupby(func, seq):
    res = []
    dict1 = {}
    for f in map(func, seq):
        for z in seq:
            if func(z) == f:
                res.append(z)
        key = f
        dict1[key] = res
        res = []
    return dict1

print(groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
