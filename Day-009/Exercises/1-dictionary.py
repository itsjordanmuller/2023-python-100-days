# Dictionary with programming terms and definitions
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Print definition of 'Bug'
print(programming_dictionary["Bug"])
# Print definition of 'Function'
print(programming_dictionary["Function"])

# Print entire dictionary
print(programming_dictionary)

# Add 'Loop' definition to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Print definition of 'Loop'
print(programming_dictionary["Loop"])
# Print updated dictionary
print(programming_dictionary)

# Iterate and print each key-value pair in the dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
