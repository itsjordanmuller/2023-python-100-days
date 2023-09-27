import sys

instructions = """Welcome to the Amazon Price Tracker
-----------------------------------
Here are your options:
1. Check prices of existing items
2. Add a new item to track
3. Remove or modify an item
4. Exit the program
-----------------------------------"""


def add_item():
    item = input("What is the name of this item?: ")
    link = input("What is the URL for this item on Amazon?: ")
    desired_price = input("What price do you want this item to drop to?: ")
    print(item, link, desired_price)


def exit_program():
    print("Thank you for using the Amazon Price Tracker. Goodbye!")
    sys.exit()


print(instructions)
selection = int(input("To choose, enter a number (1-4): "))

if selection == 1:
    pass
    # check_prices()
elif selection == 2:
    add_item()
elif selection == 3:
    pass
    # modify_item()
else:
    exit_program()
