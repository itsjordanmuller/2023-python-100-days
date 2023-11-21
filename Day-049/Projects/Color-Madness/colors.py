import random

color_dict = {
    "White": "#FFFFFF",
    "Pink": "#FFC0CB",
    "Red": "#FF0000",
    "Brown": "#7B3F00",
    "Orange": "#FFA500",
    "Yellow": "#FFFF00",
    "Green": "#228B22",
    "Blue": "#0096FF",
    "Purple": "#800080",
    "Grey": "#808080",
    "Black": "#000000",
}


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)
