# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as file:
    starting_contents = file.readlines()
    # print(starting_contents)

with open("Input/Names/invited_names.txt") as file:
    name_contents = file.readlines()
    names = []
    for name in name_contents:
        stripped_name = name.strip()
        names.append(stripped_name)
    print(names)

# with open("Output/ReadyToSend/test.txt", mode="w") as file:
#     file.write("".join(contents))
