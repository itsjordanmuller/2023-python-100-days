print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are $5")
    elif age <= 18 >= age:
        print("Youth tickets are $7")
    else:
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo taken? Y for Yes, N for No ")
    if wants_photo == "Y":
        print("Photos are an additional $3")
else:
    print("You are not tall enough to ride the rollercoaster yet, try again next time!")
