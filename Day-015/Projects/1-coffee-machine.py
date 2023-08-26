# Flavors: Espresso, Latte, Cappuccino

# Espresso $1.5 | Recipe: 50ml Water, 18g Coffee, 0ml Milk
# Latte $2.5 | Recipe: 200ml Water, 24g Coffee, 150ml Milk
# Cappuccino $3.0 | Recipe: 250ml Water, 24g Coffee, 100ml Milk

# Coffee Machine Resources: (300ml Water, 200ml Milk, 100g Coffee)

# Penny $0.01
# Nickel $0.05
# Dime $0.10
# Quarter $0.25

# Typing 'report' should give a report of the resources & money in the coffee machine
# Water: (x)ml
# Milk: (x)ml
# Coffee: (x)g
# Money: $x.xx

# Allow the user to keep ordering more, but if there's not enough of a certain resource, tell them which resource there is not enough of

# Process the coins inserted into the machine, calculating the excess and returning any money not used for the coffee, checking to make sure the transaction was successful and the user paid enough. If the transaction is successful, deduct the money from the total input and return the change.


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
        print(f"Transaction successful! Here is your change: ${change:.2f}")
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded: ${amount_entered:.2f}")
        return False


def check_resources(drink):
    """
    Returns True if resources are sufficient for the chosen drink. Otherwise, returns False and
    prints which ingredient is insufficient.
    """
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there's not enough {ingredient}.")
            return False
    return True


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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

operation = ""
status = "on"

while status == "on":
    operation = input("What would you like? (espresso/latte/cappuccino): ")
    if operation == "off":
        print("Shutting down machine.")
        status = "off"
    elif operation in ["espresso", "latte", "cappuccino"]:
        if check_resources(operation):
            print(f"You have selected a {operation}. Please insert money.")
            total_money = get_money()
            if process_transaction(total_money, MENU[operation]["cost"]):
                for ingredient, amount in MENU[operation]["ingredients"].items():
                    resources[ingredient] -= amount
                print(f"Here's your {operation} ☕ Enjoy!")
            else:
                print("Please try again with enough money.")
        else:
            print(f"Sorry, we can't make a {operation} right now.")
    elif operation == "report":
        print_report()
