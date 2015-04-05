def palindrome(p):
    str_p = str(p)
    if str_p == str_p[::-1]:
        return True
    else:
        return False

print palindrome(121)

def p_score(n):
    str_n = str(n)
    if palindrome(n):
        return 1
    else:
        return 1 + p_score(int(str_n) + int(str_n[::-1]))

print p_score(198)

