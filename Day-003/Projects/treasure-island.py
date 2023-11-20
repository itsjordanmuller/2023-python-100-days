print(
    """
████████████████████████████████████████████████
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██▓▓▓▓▓▓▓▓▓▓▓▓██    ██
██    ████████████████████████████████████    ██
██                ██        ██                ██
████████████████████  ████  ████████████████████
██    ██▓▓▓▓▓▓▓▓▓▓██  ▓▓▓▓  ██▓▓▓▓▓▓▓▓▓▓██    ██
██    ██████████████        ██████████████    ██
██                  ████████                  ██
██                                            ██
████████████████████████████████████████████████
"""
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Flow Chart Image Link
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Prompt the player to choose a direction
direction = input("Would you like to go left or right?\n").lower()

if direction == "left":
    # Scenario for choosing left
    swim = input(
        "You go to the left and come to a dock. There is an island out in the middle of the lake. Type 'Wait' to wait, or 'Swim' to swim across.\n"
    )
    if swim == "wait":
        # Scenario for waiting at the dock
        door = input(
            "You notice there is a house with 3 doors. One red, one yellow, and one blue. Which do you choose?\n"
        )
        # Consequences of door choice
        if door == "red":
            print("You enter a room full of fire and die. Game over.")
        elif door == "yellow":
            print("You find a pot of gold! You win!")
        else:
            print(
                "A wizard greets you, to tell you that you've lost. He vaporizes you with his electricity spell. Game over."
            )
    elif swim == "swim":
        # Scenario for choosing to swim
        print("You try to swim across, but you drown and die. Game over.")
else:
    # Scenario for choosing right
    print("You go to the right and are eaten by a dragon. Game over.")
