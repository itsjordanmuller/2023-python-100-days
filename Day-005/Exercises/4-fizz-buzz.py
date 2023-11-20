print("\nFizzBuzz Challenge\n")

print("---Start FizzBuzz---")
# Iterate through numbers 1 to 100
for num in range(1, 101):
    # Check if number is divisible by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # Check if number is divisible by 3
    elif num % 3 == 0:
        print("Fizz")
    # Check if number is divisible by 5
    elif num % 5 == 0:
        print("Buzz")
    # Print number if not divisible by 3 or 5
    else:
        print(num)
print("---End FizzBuzz---")
