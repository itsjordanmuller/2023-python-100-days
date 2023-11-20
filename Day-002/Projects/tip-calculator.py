print("\nTip Calculator\n")

# Prompt for and store the total bill amount
total_bill = float(input("1. What was the total bill? $"))

# Prompt for tip percentage and convert it to a decimal for calculation
tip_input = float(
    input("2. What percentage tip would you like to give? 10, 12, or 15? ")
)
tip_percent = tip_input / 100

# Prompt for and store the number of people splitting the bill
num_people = int(input("3. How many people to split the bill? "))

# Calculate and format the cost per person, including tip
cost_per_person = round((total_bill / num_people) * (1 + tip_percent), 2)
print(f"\nEach person should pay: ${cost_per_person}")
