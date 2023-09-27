import os
import sys
import json

DATA_DIR = "./data/"
ITEMS_FILE = os.path.join(DATA_DIR, "items.json")

if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

instructions = """-----------------------------------
Here are your options:
1. View all items & check prices
2. Add a new item to track
3. Remove or modify an item
4. Exit the program
-----------------------------------"""


def load_items():
    if os.path.exists(ITEMS_FILE):
        with open(ITEMS_FILE, "r") as file:
            return json.load(file)
    return []


def save_items(items):
    with open(ITEMS_FILE, "w") as file:
        json.dump(items, file, indent=2)


def add_item():
    items = load_items()

    item_name = input("What is the name of this item?: ")
    link = input("What is the URL for this item on Amazon?: ")
    desired_price = float(input("What price do you want this item to drop to?: "))

    item_data = {"item": item_name, "link": link, "desired_price": desired_price}

    items.append(item_data)
    save_items(items)

    print(f"Item {item_name} added successfully!")


def view_items():
    items = load_items()

    if not items:
        print("No items to display.")
        return

    print("Items:")
    for index, item in enumerate(items, start=1):
        print(
            f"{index}. {item['item']} - Desired price: ${item['desired_price']:.2f} - {item['link']}"
        )

    selection = int(
        input(
            "Enter the number of the item you want to check, or 0 to check all items: "
        )
    )

    if selection == 0:
        check_prices(items)
    elif 0 < selection <= len(items):
        check_prices([items[selection - 1]])
    else:
        print("Invalid input.")


def check_prices(selected_items):
    print("Checking prices for selected items...")
    for item in selected_items:
        print(item)
    print("Price checking completed.")
    input("Press Enter when you are ready to continue.")


def exit_program():
    print("Thank you for using the Amazon Price Tracker. Goodbye!")
    sys.exit()


print("Welcome to the Amazon Price Tracker!")

while True:
    print(instructions)
    selection = int(input("To choose, enter a number (1-4): "))

    if selection == 1:
        view_items()
        # check_prices()
    elif selection == 2:
        add_item()
    elif selection == 3:
        pass
        # modify_item()
    elif selection == 4:
        exit_program()
    else:
        print("Invalid input, please pick a number between 1 and 4.")
