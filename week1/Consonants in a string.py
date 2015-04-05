def count_consonants(str1):
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    count = 0
    for i in str1:
        if i in consonants:
            count += 1
    return count

print count_consonants("Python")

