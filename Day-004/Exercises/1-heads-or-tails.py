import random

print("\nFlip Coin")

heads = """
  ╔════════╗  
 ╔╝ ░░░▒▒▓ ╚╗ 
╔╝ ░░░░▒▒▓▓ ╚╗
║ ░░░HEAD▒▓▓ ║
╚╗ ░░░▒▒▒▓▓ ╔╝
 ╚╗ ░░░▒▒▓ ╔╝ 
  ╚════════╝  
"""

tails = """
  ╔════════╗  
 ╔╝ ░░░▒▒▓ ╚╗ 
╔╝ ░░░░▒▒▓▓ ╚╗
║ ░░░TAIL▒▓▓ ║
╚╗ ░░░▒▒▒▓▓ ╔╝
 ╚╗ ░░░▒▒▓ ╔╝ 
  ╚════════╝  
"""

# Generate a random integer, 0 or 1, to simulate a coin toss
face_value = random.randint(0, 1)

# Print ASCII Art, Tails for 0, Heads for 1
if face_value == 0:
    print(tails)
else:
    print(heads)
