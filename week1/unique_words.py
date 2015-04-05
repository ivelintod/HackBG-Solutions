def unique_words_count(arr):
    one_of_a_kind = 1
    for word in arr:
        count = arr.count(word)
        if count == 1:
            one_of_a_kind += 1
    return one_of_a_kind

print unique_words_count(["HELLO!"] * 10)
