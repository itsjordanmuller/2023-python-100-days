print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif 12 <= age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo taken? Y for Yes, N for No ")
    if wants_photo == "Y":
        bill += 3
        print("Photos are an additional $3")

    print(f"Your total bill is ${bill}")

else:
    print("You are not tall enough to ride the rollercoaster yet, try again next time!")
