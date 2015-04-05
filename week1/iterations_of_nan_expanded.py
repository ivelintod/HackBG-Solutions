def iterations_of_nan_expand(expanded):
    if expanded == '':
        return 0
    elif "Not " not in expanded and " a " not in expanded and " NaN" not in expanded:
        return False
    else:
        occurances = expanded.count("Not a")
        return occurances

print iterations_of_nan_expand('Not a Not a Not a NaN          ')
