def count(n):
    res = []
    count = 1
    for i in range(0, len(n) - 1):
        if n[i] == n[i + 1]:
            count += 1
        else:
            res.append(count)
            count = 1
    res.append(count)
    return res
#print count([1,1,1,2,3,1,1])

def group(seq):
    count_same = count(seq)
    result = []
    result_final = []
    i1 = 0
    for i in count_same:
        for x in range(i):
            result.append(seq[i1])
        i1 += i
        result_final.append(result)
        result = []
    return result_final

print group([1,1,1,2,3,1,1])






