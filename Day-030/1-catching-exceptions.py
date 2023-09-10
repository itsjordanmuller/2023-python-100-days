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

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     # print(a_dictionary["non-existent-key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")
#     raise TypeError("This is an error that I made up")

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Height should not be over 3 meters")

bmi = weight / height**2
print(bmi)
