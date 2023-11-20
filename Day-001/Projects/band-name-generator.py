print(
    "\nAutomatic Band Name Generator\nA state of the art Band Name Generation Utility\nBuilt with Python by Jordan Muller!\n"
)

# Get name of user's home town/city
city = input("What city/town did you grow up in?:\n")

# Get name of user's beloved pet
pet = input("What is the name of a beloved pet?\n")

# Generate and display band name suggestion
print("\nA good band name might be: 'The " + city + " " + pet + "s'")
