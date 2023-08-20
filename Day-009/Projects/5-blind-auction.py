from art import logo
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


print(logo)
print("Welcome to the blind auction program.")

bidders = []
bidding = "y"
