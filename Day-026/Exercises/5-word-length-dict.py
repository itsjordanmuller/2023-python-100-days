print("\nWord Length Dictionary Exercise\n")

# Sample sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# Split sentence into words
word_list = sentence.split()

# Create dictionary with word lengths
result = {word: len(word) for word in word_list}

# Print dictionary of words and their lengths
print(result)
