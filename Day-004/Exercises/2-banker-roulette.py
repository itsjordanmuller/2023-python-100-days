import random

print("\nBanker Roulette")
print("The game that decides who pays for dinner!\n")

# Collect comma-separated names from user
names_string = input("Give me everybody's names, separated by a commas:\n")
names = names_string.split(", ")

# Calculate index range for name selection
name_len = len(names) - 1

# Randomly select and announce who will buy the meal
print(f"\n{names[random.randint(0, name_len)]} is going to buy the meal today!")
