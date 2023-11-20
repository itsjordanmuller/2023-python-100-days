import random
from art import logo, vs
from game_data import data


# Determine if user's guess is correct
def is_guess_correct(guess, person_a_followers, person_b_followers):
    return (guess == "A" and person_a_followers > person_b_followers) or (
        guess == "B" and person_b_followers > person_a_followers
    )


# Select a random person, different from the previous one
def get_new_person(previous_person=None):
    person = random.choice(data)
    while person == previous_person:
        person = random.choice(data)
    return person


# Game introduction
print(logo)
print("Welcome to Higher or Lower!")
print("Guess which account has more followers, by choosing 'A' or 'B'")
print("Let's begin!\n")

# Initialize score and game continuation flag
score = 0
continue_game = True

# Initialize two persons for comparison
person_a = get_new_person()
person_b = get_new_person(person_a)

while continue_game:
    # Extract names and follower counts
    person_a_name, person_a_followers = person_a["name"], person_a["follower_count"]
    person_b_name, person_b_followers = person_b["name"], person_b["follower_count"]

    # Display options to user
    print(f"A: {person_a_name}{vs}\nB: {person_b_name}\n")

    # Get user guess
    guess = input("Who has more followers? A or B?: ").upper()

    # Check guess and update game state
    if is_guess_correct(guess, person_a_followers, person_b_followers):
        score += 1
        print(f"Correct! Your score is: {score}")
        person_a, person_b = person_b, get_new_person(person_b)
    elif guess in ["A", "B"]:
        print(f"Sorry, that's wrong! Your final score is: {score}")
        continue_game = False
    else:
        print("Input Error, please type 'A' or 'B'")
