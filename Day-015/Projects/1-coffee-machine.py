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

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

operation = ""
status = "on"

while status == "on":
    operation = input("What would you like? (espresso/latte/cappuccino): ")
    if operation == "off":
        print("Shutting down machine.")
        status = "off"
    elif operation == "espresso":
        print(f"You'd like to make a {operation}")
    elif operation == "latte":
        print(f"You'd like to make a {operation}")
    elif operation == "cappuccino":
        print(f"You'd like to make a {operation}")
    elif operation == "report":
        # print(f"You'd like to get a {operation}")
        print(
            f"--- Resource Report ---\nWater: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g"
        )
