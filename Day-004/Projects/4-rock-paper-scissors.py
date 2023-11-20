import random

# ASCII art for Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# ASCII art for Paper
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

# ASCII art for Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List containing rock, paper, scissors ASCII art
rock_paper_scissors = [rock, paper, scissors]

print("\nRock Paper Scissors Game\n")

# Get user's choice (adjusted for 1-based input)
user_input = (
    int(input("What do you choose?\n1. for Rock\n2. for Paper\n3. for Scissors.\n")) - 1
)

# Validate user input and play game
if user_input >= 3 or user_input < 0:
    print("Error")
else:
    # Display user's choice
    print(f"{rock_paper_scissors[user_input]}Player chooses: {user_input + 1}")
    # Generate computer's choice
    computer_input = random.randint(0, 2)
    # Display computer's choice
    print(
        f"{rock_paper_scissors[computer_input]}Computer chooses: {computer_input + 1}"
    )

    # Determine and display game outcome
    if user_input == computer_input:
        print("\nIt's a tie")
    elif user_input == 0 and computer_input == 1:
        print("\nComputer wins.")
    elif user_input == 1 and computer_input == 2:
        print("\nComputer wins.")
    elif user_input == 2 and computer_input == 0:
        print("\nComputer wins.")
    else:
        print("\nPlayer wins!")
