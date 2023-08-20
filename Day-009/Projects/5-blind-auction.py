from art import logo
import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


print(logo)
print("Welcome to the blind auction program.")

bidders = []
bidding = "y"

while bidding == "y":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders.append({"name": name, "bid": bid})
    bidding = input("Are there any other bidders? Type 'y' or 'n': ")
    if bidding == "y":
        clear()
