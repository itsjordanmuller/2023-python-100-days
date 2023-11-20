print("\nLife in Weeks Calculator\n")

# Get user's current age from input
age = input("What is your current age? ")

# Calculate remaining time in various units
# Assumes a 90-year life span
age_int = int(age)
years_remaining = 90 - age_int
months_remaining = 12 * years_remaining
weeks_remaining = 52 * years_remaining
days_remaining = 365 * years_remaining

# Display the time left in days, weeks, and months
print(
    f"\nYou have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
)
