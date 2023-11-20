import random

print("\nWelcome to the PyPassword Generator!\n")

# Define character sets for password generation
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

# User input for password composition
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Initialize empty password
password = ""

# Add random letters to password
for _ in range(num_letters):
    password += letters[random.randint(0, len(letters) - 1)] + " "

# Add random symbols to password
for _ in range(num_symbols):
    password += symbols[random.randint(0, len(symbols) - 1)] + " "

# Add random numbers to password
for _ in range(num_numbers):
    password += numbers[random.randint(0, len(numbers) - 1)] + " "

# Split password into list for shuffling
pass_list = password.split()

# Generate simple (un-shuffled) password
simple_pass = "".join(pass_list)

# Shuffle password list for complex password
random.shuffle(pass_list)

# Generate complex (shuffled) password
complex_pass = "".join(pass_list)

# Display simple and complex passwords
print(f"\nSimple: {simple_pass}")
print(f"Scrambled: {complex_pass}")
