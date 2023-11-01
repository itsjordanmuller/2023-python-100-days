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
