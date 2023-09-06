numbers = [1, 2, 3]
new_numbers = [num + 1 for num in numbers]
print(new_numbers)

name = "Jordan"
letter_list = [letter for letter in name]
print(letter_list)

range_nums = range(1, 5)
range_list = [n * 2 for n in range_nums]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
names_list = [name for name in names if len(name) <= 4]
print(names_list)
