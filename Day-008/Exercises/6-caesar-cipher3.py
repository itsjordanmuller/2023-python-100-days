alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    if direction == "encode":
        cipher_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position % 52]
            cipher_text += new_letter
        print(f"The encoded text is: {cipher_text}")
    elif direction == "decode":
        decoded_text = ""
        for letter in text:
            position = alphabet.index(letter)
            old_position = (position - shift) % 52
            decoded_text += alphabet[old_position]
        print(f"The decoded text is {decoded_text}")
    else:
        print("Wrong input")


caesar(text, shift, direction)
