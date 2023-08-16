import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_paper_scissors = [rock, paper, scissors]

user_input = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. ")
)

if user_input >= 3 or user_input < 0:
    print("Error")
else:
    print(f"{rock_paper_scissors[int(user_input)]}Player chooses: {user_input}")
    computer_input = random.randint(0, 2)
    print(
        f"{rock_paper_scissors[int(computer_input)]}Computer chooses: {computer_input}"
    )
    if user_input == computer_input:
        print("It's a tie")
    elif user_input == 0:
        if computer_input == 1:
            print("Computer wins.")
        else:
            print("Player wins!")
    elif user_input == 1:
        if computer_input == 2:
            print("Computer wins.")
        else:
            print("Player wins!")
    elif user_input == 2:
        if computer_input == 0:
            print("Computer wins.")
        else:
            print("Player wins!")
    else:
        print("Error")
