print("\nFilter Even Numbers\n")

# List of numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Filter even numbers using list comprehension
result = [num for num in numbers if num % 2 == 0]

# Print filtered even numbers
print(result)
