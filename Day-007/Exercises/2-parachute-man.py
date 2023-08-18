# Step 1

import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = ["_"] * len(chosen_word)
print(display)

# TODO-2: - Loop through each position in the chosen_word; If the letter at that position matches 'guess' then reveal that letter in the display at that position. e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_". Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# TODO-4: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display:
    guess = input("Choose a single letter: ").lower()
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter
    print(display)
print("Game over, you won!")
