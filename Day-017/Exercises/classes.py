# Naming conventions in Python
# Classes: PascalCase, Variables: snake_case, Constants: UPPERCASE
# Occasionally: camelCase


class User:
    def __init__(self, user_id, username):
        """
        Initialize a new user with user ID and username.
        Sets followers and following counts to 0.
        """
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        """
        Increment the follower count of the user being followed and the following count of the current user.
        """
        user.followers += 1
        self.following += 1


# Creating two User instances
user_1 = User("001", "Jordan")
user_2 = User("002", "Angela")

# User 1 follows User 2
user_1.follow(user_2)

# Displaying user details
print(user_1.id, user_1.username, user_1.followers, user_1.following)
print(user_2.id, user_2.username, user_2.followers, user_2.following)
