with open("file1.txt") as file:
    file_1_contents = file.read()
    # print(file_1_contents)

with open("file2.txt") as file:
    file_2_contents = file.read()
    # print(file_2_contents)

numbers_1 = set(file_1_contents.split())
numbers_2 = set(file_2_contents.split())

result = [int(num) for num in numbers_1 if num in numbers_2]

result = sorted(result, reverse=False)

# Write your code above 👆

print(result)
