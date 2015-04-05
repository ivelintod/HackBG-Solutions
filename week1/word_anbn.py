def is_an_bn(word):
    #count_a = word.count('a')
    #count_b = word.count('b')
    #res = word.split('')
    length = len(word)
    half = length / 2
    if word[0: half] == 'a' * (half) and word[half: length] == 'b' * half:
        return True
    else:
        return False

print(is_an_bn("aaaabbbb"))
