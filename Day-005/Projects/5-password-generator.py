import random

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

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = ""
for num in range(1, num_letters + 1):
    password = password + letters[random.randint(1, len(letters) - 1)] + " "

for num in range(1, num_symbols + 1):
    password = password + symbols[random.randint(1, len(symbols) - 1)] + " "

for num in range(1, num_numbers + 1):
    password = password + numbers[random.randint(1, len(numbers) - 1)] + " "

pass_list = password.split()

simple_pass = ""
complex_pass = ""

for char in pass_list:
    simple_pass = simple_pass + char

shuffle_list = random.shuffle(pass_list)

for char in pass_list:
    complex_pass = complex_pass + char

print(simple_pass)
print(complex_pass)
