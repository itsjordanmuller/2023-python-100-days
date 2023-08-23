import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

secret_number = random.randint(1, 100)
print(f"Psst! The number is {secret_number}")

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Error, please input 'easy' or 'hard'")

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == secret_number:
        "You got it! The answer was {guess}."
    elif guess < secret_number:
        print("Too low.\nGuess again.")
        attempts -= 1
    elif guess > secret_number:
        print("Too high.\nGuess again.")
        attempts -= 1
