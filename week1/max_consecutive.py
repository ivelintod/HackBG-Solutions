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

def max_consecutive(items):
    group_items = group(items)
    max1 = len(group_items[0])
    for i in group_items:
        if max1 <= len(i):
            max1 = len(i)
    return max1

print max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3])
