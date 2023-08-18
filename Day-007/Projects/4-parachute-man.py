import random

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

stages = stages[::-1]

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

chosen_word = random.choice(word_list)


display = ["_"] * len(chosen_word)
print(display)

lives = 6

while "_" in display and lives > 0:
    print(stages[6 - lives])
    guess = input("Choose a single letter: ").lower()
    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left.")
    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = letter
    print(display)

if lives == 0:
    print(result[0])
else:
    print(result[1])
