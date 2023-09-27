instructions = "Welcome to the Amazon Price Tracker\n-----------------------------------\nHere are your options:\n1. Check prices of existing items\n2. Add a new item to track\n3. Remove or modify an item\n4. Exit the program\n-----------------------------------"


def add_item():
    item = input("What is the name of this item?: ")
    link = input("What is the URL for this item on Amazon?: ")
    desired_price = input("What price do you want this item to drop to?: ")
    print(item, link, desired_price)


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
    pass
    # exit_program()
