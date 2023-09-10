# # File Not Found Error
# with open("a_file.txt") as file:
#     file.read()

# Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existent-key"]

# Index Error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# Type Error
# text = "abc"
# print(text + 5)

# Try: Something that might cause an exception
# Except: Do this if there was an exception
# Else: Do this if there were no exceptions
# Finally: Do this no matter what happens

try:
    file = open("a_file.txt")
except:
    print("There was an error")
