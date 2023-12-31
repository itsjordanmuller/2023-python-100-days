import random
from art import logo

# Display game logo and welcome message
print(logo)
print("\nNumber Guessing Game\n")
print("I'm thinking of a number between 1 and 100.")

# Initialize difficulty and prompt for user input
difficulty = ""
while difficulty not in ["easy", "hard"]:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty not in ["easy", "hard"]:
        print("Error, please input 'easy' or 'hard'")

# Generate a random secret number
secret_number = random.randint(1, 100)
# print(f"Psst! The number is {secret_number}")

# Set attempts based on difficulty
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

# Main game loop
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    # Check guess and provide feedback
    if guess == secret_number:
        print(f"You got it! The answer was {secret_number}.")
        break
    elif guess < secret_number:
        print("Too low.\nGuess again.")
    else:
        # Guess is too high
        print("Too high.\nGuess again.")

    # Decrement attempts after each guess
    attempts -= 1

# Inform the user if they run out of attempts
if attempts == 0:
    print("You've run out of guesses, you lose.")
    print(f"In case you were curious, the number was {secret_number}")
