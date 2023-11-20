from art import logo
import os


# Function to clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# Display logo and introduction message
print(logo)
print("\nBlind Auction Service\n")

# Initialize list to store bidders
bidders = []

# Flag to control bidding loop
bidding = "y"

# Loop to collect bids
while bidding == "y":
    # Get bidder's name and bid amount
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    # Add bidder's details to the list
    bidders.append({"name": name, "bid": bid})

    # Check if there are more bidders
    bidding = input("Are there any other bidders? Type 'y' or 'n': ")

    # Clear screen if more bidders
    if bidding == "y":
        clear()

# Determine the winner with the highest bid
winner = max(bidders, key=lambda x: x["bid"])

# Display winner's details
print("\nThe winner is", winner["name"], "with a bid of $" + str(winner["bid"]))
