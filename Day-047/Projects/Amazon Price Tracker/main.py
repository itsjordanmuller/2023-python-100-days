import os
import sys
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

DATA_DIR = "./data/"
ITEMS_FILE = os.path.join(DATA_DIR, "items.json")

if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)

instructions = """-----------------------------------
Here are your options:
1. View all items & check prices
2. Add a new item to track
3. Modify or remove an item
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

    item_data = {
        "item": item_name,
        "link": link,
        "desired_price": desired_price,
        "history": [],
    }

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


from datetime import datetime


def check_prices(selected_items):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print("Checking prices for selected items...")

    for item in selected_items:
        url = item["link"]
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            print(soup)

            price_whole_tag = soup.select_one("span.a-price-whole")
            price_fraction_tag = soup.select_one("span.a-price-fraction")

            if price_whole_tag and price_fraction_tag:
                price = float(
                    price_whole_tag.text.replace(",", "").strip()
                    + "."
                    + price_fraction_tag.text.strip()
                )
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item["history"].append({"date": date, "price": price})

                print(
                    f"Item: {item['item']}, Current Price: ${price}, Desired Price: ${item['desired_price']}"
                )

                if price <= item["desired_price"]:
                    print(
                        f"Great! {item['item']} is now at or below your desired price!"
                    )

            else:
                print(f"Could not find the price for {item['item']}.")
        else:
            print(f"Failed to retrieve data for {item['item']}.")

    save_items(selected_items)
    print("Price checking completed.")
    input("Press Enter when you are ready to continue.")


def modify_item():
    items = load_items()

    if not items:
        print("No items to modify.")
        return

    print("Items:")
    for index, item in enumerate(items, start=1):
        print(
            f"{index}. {item['item']} - Desired price: ${item['desired_price']:.2f} - {item['link']}"
        )

    selection = int(input("Enter the number of the item you want to modify: "))

    if 0 < selection <= len(items):
        selected_item = items[selection - 1]

        action = input(
            f"Do you want to modify or delete {selected_item['item']}? (modify/delete): "
        ).lower()

        if action == "modify":
            print("What do you want to modify?")
            print("1. Name")
            print("2. Link")
            print("3. Desired price")
            print("4. All")

            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                selected_item["item"] = input("Enter the new name: ")
            elif choice == 2:
                selected_item["link"] = input("Enter the new link: ")
            elif choice == 3:
                selected_item["desired_price"] = float(
                    input("Enter the new desired price: ")
                )
            elif choice == 4:
                selected_item["item"] = input("Enter the new name: ")
                selected_item["link"] = input("Enter the new link: ")
                selected_item["desired_price"] = float(
                    input("Enter the new desired price: ")
                )
            else:
                print("Invalid choice.")
                return

            print(f"Item {selected_item['item']} updated successfully!")

        elif action == "delete":
            confirm = input(
                f"Are you sure you want to delete {selected_item['item']}? (yes/no): "
            ).lower()
            if confirm == "yes":
                items.remove(selected_item)
                print(f"Item {selected_item['item']} deleted successfully!")
            elif confirm == "no":
                print("Operation cancelled.")
                return
            else:
                print("Invalid choice.")
                return
        else:
            print("Invalid action.")
            return

        save_items(items)

    else:
        print("Invalid selection.")
        return


def exit_program():
    print("Thank you for using the Amazon Price Tracker. Goodbye!")
    sys.exit()


print("Welcome to the Amazon Price Tracker!")

while True:
    print(instructions)
    selection = int(input("To choose, enter a number (1-4): "))

    if selection == 1:
        view_items()
    elif selection == 2:
        add_item()
    elif selection == 3:
        modify_item()
    elif selection == 4:
        exit_program()
    else:
        print("Invalid input, please pick a number between 1 and 4.")
