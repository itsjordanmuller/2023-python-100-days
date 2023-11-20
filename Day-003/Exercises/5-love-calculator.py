print("\nPython Love Calculator\n")

# Get names from user
name1 = input("What is your name?: ")
name2 = input("What is their name?: ")

# Combine and convert names to lowercase
combined_name = name1 + name2
lower_name = combined_name.lower()

# Count & total occurrences of each letter for "TRUE" & "LOVE"
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

true = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

love = l + o + v + e

# Combine both parts of score
love_score = int(str(true) + str(love))

# Output compatibility message based on specific score thresholds
if love_score <= 25:
    print(f"\nYour score is {love_score}. You might need more sparks to fly.")
elif love_score <= 50:
    print(f"\nYour score is {love_score}. There's potential for something great.")
elif love_score <= 75:
    print(f"\nYour score is {love_score}. You two are quite compatible!")
else:
    print(f"\nYour score is {love_score}. It's a perfect match!")
