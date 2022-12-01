def sequential_map(*args):
    *funcs, list_with_values = args
    for func in funcs:
        list_with_values = map(func, list_with_values)
    return list(list_with_values)


def consensus_filter(*args):
    *funcs, list_with_values = args
    for func in funcs:
        list_with_values = filter(func, list_with_values)
    return list(list_with_values)


def conditional_reduce(func_1, func_2, list_with_values):
    list_with_values = list(filter(func_1, list_with_values))
    res = 0
    for value in list_with_values:
        res = func_2(res, value)
    return res


def func_chain(*args):
    def result_function(x):
        for func in args:
            x = func(x)
        return x
    return result_function


