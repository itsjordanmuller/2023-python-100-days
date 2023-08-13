# Data Types

string = "Hello"
print(string[0])
print(string[len(string) - 1])

integer = 123
print(integer)
print(integer + 345)

flt = 3.14159
print(flt * 10)

num_char = len(input("What is your name?\n"))
print(type(num_char))

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters")

a = float(123)
print(type(a))

print(70 + float("100.5"))
