# Classes should use PascalCase
# Most other Python code use snake_case
# For constants, we can use UPPERCASE
# Sometimes, we also use camelCase


class User:
    # pass
    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0

    def increment_followers(self):
        self.followers += 1


user_1 = User("001", "Jordan")
# user_1.id = "001"
# user_1.username = "Jordan"

user_1.increment_followers()
print(user_1.id, user_1.username, user_1.followers)

user_2 = User("002", "Angela")
print(user_2.id, user_2.username, user_2.followers)
