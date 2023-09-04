with open("data.txt", mode="w") as file:
    file.write("New line of text!")

with open("data.txt", mode="a") as file:
    file.write("\nAnother line of text!")

with open("new_data.txt", mode="w") as file:
    file.write("Here's a new file!\nIt got created because it didn't already exist!")

# file = open("data.txt")
with open("data.txt") as file:
    contents = file.read()
    print(contents)
# file.close()
