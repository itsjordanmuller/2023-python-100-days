print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You are not tall enough to ride the rollercoaster yet, try again next time!")
