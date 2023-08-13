# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
age_int = int(age)
years_remaining = 90 - age_int
months_remaining = 12 * years_remaining
weeks_remaining = 52 * years_remaining
days_remaining = 365 * years_remaining

print(
    f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
)
