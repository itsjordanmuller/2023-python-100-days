MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


def encrypt(text):
    cipher = ""
    for letter in text.upper():
        if letter == " ":
            cipher += " "
        else:
            cipher += MORSE_CODE_DICT[letter] + " "
    return cipher


def decrypt(morse_code):
    morse_code += " "
    text = ""
    morse_char = ""
    for letter in morse_code:
        if letter != " ":
            morse_char += letter
        else:
            if morse_char:
                text += [
                    key for key, value in MORSE_CODE_DICT.items() if value == morse_char
                ][0]
                morse_char = ""
            else:
                text += " "
    return text.strip()


print("\n----- Morse Code Translator -----")
print("(WILL CONVERT TEXT TO UPPERCASE)")

while True:
    choice = input(
        "\nWhat would you like to translate?\n1. Text to Morse\n2. Morse to Text\n\n0. Exit\n\nEnter a #: "
    )

    if choice == "1":
        text = input("\nInput text to translate to Morse Code:\n")
        morse = encrypt(text)
        print(f"\n{text.upper()} in Morse: {morse}")
        print(f"{morse} in Text: {decrypt(morse)}")
    elif choice == "2":
        morse = input("\nInput Morse Code to translate to Text:\n")
        text = decrypt(morse)
        print(f"\n{morse} in Text: {text.upper()}")
        print(f"{text.upper()} in Morse: {encrypt(text)}")
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("\nInvalid Choice. Please select 1, 2, or 0 to exit.")
