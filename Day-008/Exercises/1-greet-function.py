name = input("What is the name of the person you are greeting? ")
location = input("Where do they live? ")


def greet(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")
    print(f"Isn't it lovely out today, {name}?")


greet(name, location)
