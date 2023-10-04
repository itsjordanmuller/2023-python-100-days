import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970

# Write your code below 👇


def speed_calc_decorator(function):
    def time_difference():
        time1 = time.time()
        function()
        time2 = time.time()
        diff = time2 - time1
        print(f"{function.__name__} run speed: {diff}s")

    return time_difference


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
