def count_words(arr):
    dict1 = {}
    for word in arr:
        count = arr.count(word)
        dict1[word] = count
    return dict1
print count_words(["apple", "banana", "apple", "pie"])
