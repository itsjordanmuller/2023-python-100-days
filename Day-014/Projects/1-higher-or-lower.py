import random
from art import logo, vs
from game_data import data


def is_guess_correct(guess, person_a_followers, person_b_followers):
    """
    Returns True if the guess is correct; otherwise, returns False.
    """
    if guess == "A" and person_a_followers > person_b_followers:
        return True
    elif guess == "B" and person_b_followers > person_a_followers:
        return True
    return False


print(logo)
print("Welcome to Higher or Lower!")
print(
    "You will guess which account has more followers, by entering either 'A' or 'B' to make a guess"
)
print("Let's begin!\n")

score = 0
continue_game = True

person_a = random.choice(data)
person_b = random.choice(data)
while person_b == person_a:
    person_b = random.choice(data)

while continue_game:
    person_a_name = person_a["name"]
    person_b_name = person_b["name"]
    person_a_followers = person_a["follower_count"]
    person_b_followers = person_b["follower_count"]

    print(f"A: {person_a_name}{vs}\nB: {person_b_name}\n")
    guess = input("Who has more followers? A or B?: ").upper()

    if is_guess_correct(guess, person_a_followers, person_b_followers):
        score += 1
        print(f"Correct! Your score is: {score}")
        person_a = person_b
        person_b = random.choice(data)
        while person_b == person_a:
            person_b = random.choice(data)
    elif guess in ["A", "B"]:
        print(f"Sorry, that's wrong! Your final score is: {score}")
        continue_game = False
    else:
        print("Input Error, please type 'A' or 'B'")
