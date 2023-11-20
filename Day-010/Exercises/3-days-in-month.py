def is_leap(year):
    # Check for leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    # Days in each month
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Adjust for leap year in February
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


print("\nDays in Month Calculator\n")
print("Check how many days are in a specific month in a specific year:")
print("\nEnter Year as YYYY, Month as M")

# User input for year and month
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

# Calculate and print the number of days in the given month
days = days_in_month(year, month)
print(f"\n{days}")
