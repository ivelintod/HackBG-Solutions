def reduce_file_path(path):
    string = path
    slash = "/"
    one_dot = "."
    two_dots = ".."
    if path == slash:
        return slash
    else:
        res = string.split("/")
        count_space = res.count('')
        count_one_dot = res.count(one_dot)
        count_two_dots = res.count(two_dots)
        for dot in range(count_one_dot):
            res.remove(one_dot)
        for dots in range(count_two_dots):
            dot_index = res.index(two_dots)
            temp = res[dot_index - 1]
            if temp != '':
                res.remove(temp)
            res.remove(two_dots)
        for space in range(count_space):
            res.remove('')
    return slash + ('/'.join(res)).strip(slash)


print reduce_file_path("/etc/../etc/../etc/../")
