def is_credit_card_valid(number):
    list1 = list(str(number))
    sum_of_digits = 0
    for i in range(0, len(list1)):
        if i % 2 != 0:
            list1[i] = int(list1[i]) * 2
            temp = len(str(list1[i]))
            if temp > 1:
                sum_of_digits += temp - 1
    for i in range(0, len(list1)):
        sum_of_digits += int(list1[i])
    if sum_of_digits % 10 == 0:
        return True
    else:
        return False


print is_credit_card_valid(79927398713)
