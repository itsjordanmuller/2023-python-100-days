def print_report():
    """Prints the current resource report."""
    print(
        f"--- Resource Report ---\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']:.2f}"
    )


def get_money():
    """Asks the user to input their values of each coin, and calculates the total input value"""
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_input = (
        (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    )
    return total_input


def process_transaction(amount_entered, drink_cost):
    """
    Process the money transaction.
    If the user has input enough money, update the money resource, deduct the drink cost, and return the change.
    If not, let the user know they haven't input enough money.
    """
    if amount_entered >= drink_cost:
        change = amount_entered - drink_cost
        resources["money"] += drink_cost
        print(f"\nTransaction successful! Here is your change: ${change:.2f}")
        return True
    else:
        print(
            f"\nSorry, that's not enough money. Money refunded: ${amount_entered:.2f}"
        )
        return False


def check_resources(drink):
    """
    Returns True if resources are sufficient for the chosen drink. Otherwise, returns False and
    prints which ingredient is insufficient.
    """
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"\nSorry, there's not enough {ingredient}.")
            return False
    return True


# Define menu items and their requirements
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

# Initialize resource levels
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# Initialize Values for Status & Operation
operation = ""
status = "on"

print("\nCoffee Machine Simulator")
print("Type 'report' to view resources, 'off' to exit")

while status == "on":
    operation = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    if operation == "off":
        # Turn off machine
        print("\nShutting down machine.")
        status = "off"
    elif operation in ["espresso", "latte", "cappuccino"]:
        # Process drink order if resources sufficient
        if check_resources(operation):
            print(f"You have selected a {operation}. Please insert money.\n")
            total_money = get_money()
            if process_transaction(total_money, MENU[operation]["cost"]):
                # Deduct used resources and serve drink
                for ingredient, amount in MENU[operation]["ingredients"].items():
                    resources[ingredient] -= amount
                print(f"Here's your {operation} ☕ Enjoy!")
            else:
                print("\nPlease try again with enough money.")
        else:
            print(f"Sorry, we can't make a {operation} right now.\n")
    elif operation == "report":
        # Display resource report
        print_report()
