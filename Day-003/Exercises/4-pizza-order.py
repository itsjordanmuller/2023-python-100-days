print("\nWelcome to Python Pizza Deliveries!\n")

# Get pizza size choice from user
size = input("What size pizza do you want? S, M, or L ")

# Ask user if they want pepperoni & extra cheese
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Set price to zero to start
price = 0

# Calculate price based on size and add-ons
if size == "S":
    price += 15
    if add_pepperoni == "Y":
        price += 2
elif size == "M":
    price += 20
    if add_pepperoni == "Y":
        price += 3
else:
    price += 25
    if add_pepperoni == "Y":
        price += 3

# Add extra cheese cost if chosen
if extra_cheese == "Y":
    price += 1

# Display final bill
print(f"\nYour final bill is: ${price}.")
