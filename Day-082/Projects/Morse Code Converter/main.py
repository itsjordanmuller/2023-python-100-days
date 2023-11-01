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
    unrecognized_chars = set()

    for letter in text.upper():
        if letter == " ":
            cipher += "   "
        elif letter in MORSE_CODE_DICT:
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            unrecognized_chars.add(letter)

    error_msg = (
        f"Error: {''.join(unrecognized_chars)} are not recognized or supported."
        if unrecognized_chars
        else ""
    )
    return cipher, error_msg


def decrypt(morse_code):
    text = ""
    unrecognized_morse = set()
    morse_chars = morse_code.split(" ")

    for morse_char in morse_chars:
        if not morse_char:
            text += " "
        elif morse_char in MORSE_CODE_DICT.values():
            text += [
                key for key, value in MORSE_CODE_DICT.items() if value == morse_char
            ][0]
        else:
            unrecognized_morse.add(morse_char)

    error_msg = (
        f"Error: {' '.join(unrecognized_morse)} are not recognized or supported Morse codes."
        if unrecognized_morse
        else ""
    )
    return text.strip(), error_msg


print("\n----- Morse Code Translator -----")
print("(WILL CONVERT TEXT TO UPPERCASE)")

while True:
    choice = input(
        "\nWhat would you like to translate?\n1. Text to Morse\n2. Morse to Text\n\n0. Exit\n\nEnter a #: "
    )

    if choice == "1":
        text = input("\nInput text to translate to Morse Code:\n")
        morse, error_msg = encrypt(text)
        print(f"\n{text.upper()} in Morse: {morse}")
        if error_msg:
            print(error_msg)
    elif choice == "2":
        morse = input("\nInput Morse Code to translate to Text:\n")
        text, error_msg = decrypt(morse)
        print(f"\n{morse} in Text: {text.upper()}")
        if error_msg:
            print(error_msg)
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("\nInvalid Choice. Please select 1, 2, or 0 to exit.")
