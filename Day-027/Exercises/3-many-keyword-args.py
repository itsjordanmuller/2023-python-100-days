def calculate(n, **kwargs):
    print(kwargs)
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"], kwargs["multiply"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
