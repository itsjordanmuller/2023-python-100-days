print("\nBMI Calculator\n")

# Prompt for and store user's height/weight
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

# Convert height and weight from string to float for calculation
height_float = float(height)
weight_float = float(weight)

# Calculate BMI using Formula:
# Formula: weight (kg) / (height (m)^2)
bmi = weight_float / (height_float**2)

# Display the calculated BMI as an integer
print("\nYour BMI is:")
print(int(bmi))
