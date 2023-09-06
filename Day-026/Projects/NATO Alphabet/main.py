import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)
# print(df)
phonetic_dict = {row["letter"]: row["code"] for (index, row) in df.iterrows()}
# print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

print("Welcome to the NATO Phonetic Conversion Tool")
user_input = input("What word would you like to convert to the NATO Alphabet?\n")
letter_list = [letter for letter in user_input]
print(letter_list)
