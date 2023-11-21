print("\nList Comprehension Exercise\n")

# Increment each number in the list by 1
numbers = [1, 2, 3]
new_numbers = [num + 1 for num in numbers]
print(new_numbers)

# Convert each letter in name to list item
name = "Jordan"
letter_list = [letter for letter in name]
print(letter_list)

# Double each number in specified range
range_nums = range(1, 5)
range_list = [n * 2 for n in range_nums]
print(range_list)

# Create list of names with <= 4 characters
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
names_list = [name for name in names if len(name) <= 4]
print(names_list)

# Uppercase names with >= 5 characters
upper_names_list = [name.upper() for name in names if len(name) >= 5]
print(upper_names_list)
