def add(*args):
    print(args[1])
    sum_args = 0
    for arg in args:
        sum_args += arg
        # print(arg)
    return sum_args


print(add(5, 6, 11))
