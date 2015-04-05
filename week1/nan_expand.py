def nan_expand(times):
    final_result = ""
    if times == 0:
        return final_result
    elif times > 0:
        final_result = "NaN"
        for i in range(0, times):
            temp = "Not a "
            final_result = temp + final_result
        return final_result

print nan_expand(2)
