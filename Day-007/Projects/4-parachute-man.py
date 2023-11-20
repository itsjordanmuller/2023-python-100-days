import random

print("\nParachute Man Word Guessing Game\n")

result = [
    """
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
      
 YOU FELL DOWN

  YOU  LOSE

      O
     /|\ 
     / \ 

==============
""",
    """

 YOU MADE IT
 DOWN SAFELY

   YOU WIN

      O
     /|\ 
     / \ 
==============
""",
]

stages = [
    """
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
      |
      |
      O
     /|\ 
     / \ 

==============
""",
    """
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
   \     /
    \   /
     \O/
     /|\ 
     / \ 

==============
""",
    """
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
   \ /   /
    \   /
     \O/
     /|\ 
     / \ 

==============
""",
    """
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
   \ / \ /
    \   /
     \O/
     /|\ 
     / \ 

==============
""",
    """
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
   \ / \|/
    \   /
     \O/
     /|\ 
     / \ 

==============
""",
    """
     ___
   _/   \_
 _/ \___/ \_
 \  /   \  /
  \/_____\/
   \|/ \|/
    \   /
     \O/
     /|\ 
     / \ 

==============
""",
]

# Reverse the order of the hangman stages
stages = stages[::-1]

# List of Possible Words for the Game
word_list = [
    "abruptly",
    "absurd",
    "abyss",
    "affix",
    "askew",
    "avenue",
    "awkward",
    "axiom",
    "azure",
    "bagpipes",
    "bandwagon",
    "banjo",
    "bayou",
    "beekeeper",
    "bikini",
    "blitz",
    "blizzard",
    "boggle",
    "bookworm",
    "boxcar",
    "boxful",
    "buckaroo",
    "buffalo",
    "buffoon",
    "buxom",
    "buzzard",
    "buzzing",
    "buzzwords",
    "caliph",
    "cobweb",
    "cockiness",
    "croquet",
    "crypt",
    "curacao",
    "cycle",
    "daiquiri",
    "dirndl",
    "disavow",
    "dizzying",
    "duplex",
    "dwarves",
    "embezzle",
    "equip",
    "espionage",
    "euouae",
    "exodus",
    "faking",
    "fishhook",
    "fixable",
    "fjord",
    "flapjack",
    "flopping",
    "fluffiness",
    "flyby",
    "foxglove",
    "frazzled",
    "frizzled",
    "fuchsia",
    "funny",
    "gabby",
    "galaxy",
    "galvanize",
    "gazebo",
    "giaour",
    "gizmo",
    "glowworm",
    "glyph",
    "gnarly",
    "gnostic",
    "gossip",
    "grogginess",
    "haiku",
    "haphazard",
    "hyphen",
    "iatrogenic",
    "icebox",
    "injury",
    "ivory",
    "ivy",
    "jackpot",
    "jaundice",
    "jawbreaker",
    "jaywalk",
    "jazziest",
    "jazzy",
    "jelly",
    "jigsaw",
    "jinx",
    "jiujitsu",
    "jockey",
    "jogging",
    "joking",
    "jovial",
    "joyful",
    "juicy",
    "jukebox",
    "jumbo",
    "kayak",
    "kazoo",
    "keyhole",
    "khaki",
    "kilobyte",
    "kiosk",
    "kitsch",
    "kiwifruit",
    "klutz",
    "knapsack",
    "larynx",
    "lengths",
    "lucky",
    "luxury",
    "lymph",
    "marquis",
    "matrix",
    "megahertz",
    "microwave",
    "mnemonic",
    "mystify",
    "naphtha",
    "nightclub",
    "nowadays",
    "numbskull",
    "nymph",
    "onyx",
    "ovary",
    "oxidize",
    "oxygen",
    "pajama",
    "peekaboo",
    "phlegm",
    "pixel",
    "pizazz",
    "pneumonia",
    "polka",
    "pshaw",
    "psyche",
    "puppy",
    "puzzling",
    "quartz",
    "queue",
    "quips",
    "quixotic",
    "quiz",
    "quizzes",
    "quorum",
    "razzmatazz",
    "rhubarb",
    "rhythm",
    "rickshaw",
    "schnapps",
    "scratch",
    "shiv",
    "snazzy",
    "sphinx",
    "spritz",
    "squawk",
    "staff",
    "strength",
    "strengths",
    "stretch",
    "stronghold",
    "stymied",
    "subway",
    "swivel",
    "syndrome",
    "thriftless",
    "thumbscrew",
    "topaz",
    "transcript",
    "transgress",
    "transplant",
    "triphthong",
    "twelfth",
    "twelfths",
    "unknown",
    "unworthy",
    "unzip",
    "uptown",
    "vaporize",
    "vixen",
    "vodka",
    "voodoo",
    "vortex",
    "voyeurism",
    "walkway",
    "waltz",
    "wave",
    "wavy",
    "waxy",
    "wellspring",
    "wheezy",
    "whiskey",
    "whizzing",
    "whomever",
    "wimpy",
    "witchcraft",
    "wizard",
    "woozy",
    "wristwatch",
    "wyvern",
    "xylophone",
    "yachtsman",
    "yippee",
    "yoked",
    "youthful",
    "yummy",
    "zephyr",
    "zigzag",
    "zigzagging",
    "zilch",
    "zipper",
    "zodiac",
    "zombie",
]

# Randomly select a word from the list
chosen_word = random.choice(word_list)

# Initialize the display with underscores representing each letter of the chosen word
display = ["_"] * len(chosen_word)
print(display)

# Set initial number of lives
lives = 6

# Game loops until all letters are guessed or lives run out
while "_" in display and lives > 0:
    # Display current stage of hangman
    print(stages[6 - lives])

    # Get player's letter guess
    guess = input("Choose a single letter: ").lower()

    # Decrease a life if the guess is incorrect
    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left.")

    # Reveal correctly guessed letters in the display
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter
    print(display)

# End of game messages (assuming 'result' is predefined with victory/loss messages)
if lives == 0:
    # Game Loss
    print(result[0])
else:
    # Game Won
    print(result[1])
