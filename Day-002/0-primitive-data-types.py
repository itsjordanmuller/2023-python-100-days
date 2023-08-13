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

print(str(70) + str(100))

print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 3)
print(2**3)

# PEMDAS
# ()
# **
# * /
# + -

print(int(8 / 3))
print(round(8 / 3))
print(round(8 / 3, 2))
print(8 // 3)

result = 8 / 2
result /= 2
print(result)

score = 0
score += 1
print(score)
height = 1.8
isWinning = True

print(
    f"Your score is {score}, your height is {height}, and you are winning is: {isWinning}"
)
