def calculate(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)


calculate(add=3, multiply=5)
