import random

color_list = [
    "White",
    "Pink",
    "Red",
    "Brown",
    "Orange",
    "Yellow",
    "Green",
    "Blue",
    "Purple",
    "Grey",
    "Black",
]


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)
