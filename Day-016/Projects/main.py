from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize objects for money handling, coffee making, and menu
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Flag to keep the machine running
is_on = True

print("\nCoffee Machine Simulator")
print("Type 'report' to view resources, 'off' to exit")

# Main loop for coffee machine operations
while is_on:
    # Retrieve menu items
    options = menu.get_items()
    # Get user's choice
    choice = input(f"\nWhat would you like? ({options}): ")

    if choice == "off":
        # Turn off the machine
        print("\nShutting down machine.")
        is_on = False
    elif choice == "report":
        # Display reports for coffee maker and money machine
        print("--- Resource Report ---")
        coffee_maker.report()
        money_machine.report()
    else:
        # Find the drink object based on user's choice
        drink = menu.find_drink(choice)
        # Check resource sufficiency and process payment
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            # Make and serve coffee
            coffee_maker.make_coffee(drink)
