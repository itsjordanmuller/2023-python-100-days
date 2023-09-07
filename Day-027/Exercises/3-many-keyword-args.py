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


# calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="Nissan", model="GT-R")
print(f"Make: {my_car.make} | Model: {my_car.model}")
