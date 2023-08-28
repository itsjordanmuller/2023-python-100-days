# Classes should use PascalCase
# Most other Python code use snake_case
# For constants, we can use UPPERCASE
# Sometimes, we also use camelCase


class User:
    # pass
    def __init__(self):
        print("New user being created...")


user_1 = User()
user_1.id = "001"
user_1.username = "Jordan"

print(user_1.id, user_1.username)
