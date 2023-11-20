print("\nBMI Calculator v2\n")

# Get user's height & height values
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# Calculate BMI and round it
bmi = round((weight) / (height**2))

# Determine and display BMI category
if bmi < 18.5:
    print(f"\nYour BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"\nYour BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"\nYour BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"\nYour BMI is {bmi}, you are obese.")
else:
    print(f"\nYour BMI is {bmi}, you are clinically obese.")
