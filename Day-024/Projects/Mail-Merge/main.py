# Read starting letter template
with open("Input/Letters/starting_letter.txt") as file:
    starting_contents = file.read()

# Read invited names and clean data
with open("Input/Names/invited_names.txt") as file:
    name_contents = file.readlines()
    names = [name.strip() for name in name_contents]

# Generate personalized letters for each name
for name in names:
    personalized_letter = starting_contents.replace("[name]", name)

    # Save personalized letters to files
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as file:
        file.write(personalized_letter)
