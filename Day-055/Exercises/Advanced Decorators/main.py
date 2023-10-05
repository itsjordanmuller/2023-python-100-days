## Simple Python Decorator Functions
# import time


# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         # Do something before
#         function()
#         function()
#         # Do something after

#     return wrapper_function


# @delay_decorator
# def say_hello():
#     print("Hello")


# With the @ syntactic sugar
# @delay_decorator
# def say_bye():
#     print("Bye")


# Without the @ syntactic sugar
# def say_greeting():
#     print("How are you?")


# decorated_function = delay_decorator(say_greeting)
# decorated_function()


# Advanced Python Decorator Functions


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def authenticate(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])

    return authenticate


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Jordan")
new_user.is_logged_in = True
create_blog_post(new_user)


# Logging Decorator Challenge

inputs = eval(input())


def logging_decorator(function):
    def log(*args, **kwargs):
        result = function(*args, **kwargs)
        print(f"You called {function.__name__}({args})\nIt returned: {result}")

    return log


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
