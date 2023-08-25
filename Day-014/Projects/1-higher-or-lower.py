import random
from art import logo, vs
from game_data import data

print(logo)
print("Welcome to Higher or Lower!")
print(
    "You will guess which account has more followers, by entering either 'A' or 'B' to make a guess"
)
print("Let's begin!\n")

random_entry = random.choice(data)

person_a = random.choice(data)
person_b = random.choice(data)

while person_b == person_a:
    person_b = random.choice(data)

person_a_name = person_a["name"]
person_b_name = person_b["name"]
person_a_followers = person_a["follower_count"]
person_b_followers = person_b["follower_count"]

print(f"A: {person_a_name}{vs}\nB: {person_b_name}\n")
guess = input("Who has more followers? A or B?: ")
