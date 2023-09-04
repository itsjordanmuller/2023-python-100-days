with open("data.txt", mode="w") as file:
    file.write("New line of text!")

# file = open("data.txt")
with open("data.txt") as file:
    contents = file.read()
    print(contents)
# file.close()
