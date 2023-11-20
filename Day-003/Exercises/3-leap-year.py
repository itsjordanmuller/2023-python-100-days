print("\nLeap Year Checker\n")

# Get user input for the year
year = int(input("Which year do you want to check? "))

# Check if year is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            # Divisible by 400: Leap year
            print(f"\n{year} is a leap year.")
        else:
            # Divisible by 100 but not 400: Not a leap year
            print(f"\n{year} is not a leap year.")
    else:
        # Divisible by 4 but not 100: Leap year
        print(f"\n{year} is a leap year.")
else:
    # Not divisible by 4: Not a leap year
    print(f"\n{year} is not a leap year.")
