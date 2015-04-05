def p_score(n):
    n_str = str(n)
    list1 = list(n_str)
    result = []
    length_list1 = len(list1)

    for letters in list1:
        last = list1[length_list1 - 1]
        result.append(last)
        length_list1 -= 1
    final_result = ''.join(result)


    start_i = 0
    end_i = len(n_str)
    for i in n_str:
        if n_str[start_i] == n_str[end_i - 1]:
            start_i += 1
            end_i -= 1
            result1 = 1
    else:
        result1 = 1 + p_score(n_str + final_result)

    return result1




