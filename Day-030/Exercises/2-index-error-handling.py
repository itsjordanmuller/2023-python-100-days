fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
        return fruit + " pie"
    except IndexError:
        print("Fruit pie")
        return "Fruit pie"


try:
    make_pie(4)
except IndexError:
    print("Fruit pie")
