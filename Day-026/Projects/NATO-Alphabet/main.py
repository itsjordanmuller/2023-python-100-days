import pandas

# Load NATO Phonetic Alphabet data
data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)

# Create dictionary from data: letters as keys, codes as values
phonetic_dict = {row["letter"]: row["code"] for (index, row) in df.iterrows()}

print("\nNATO Phonetic Conversion Tool\n")

# Loop to convert user input into NATO phonetic alphabet
while True:
    user_input = input("What word would you like to convert to the NATO Alphabet?\n")
    letter_list = [letter for letter in user_input]

    try:
        # Convert each letter in user input to its NATO phonetic equivalent
        converted_list = [
            phonetic_dict[letter.upper()]
            for letter in letter_list
            if letter.upper() in phonetic_dict
        ]

        # Check if all characters in user input are valid and display result
        if len(converted_list) == len(letter_list):
            print(" ".join(converted_list))
            break
        else:
            print("Sorry, only letters in the alphabet please.")
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
