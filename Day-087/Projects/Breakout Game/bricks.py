from turtle import Turtle

BRICK_CONFIGS = {
    "small": {
        "width": 20,
        "height": 20,
        "padding": 5,
        "per_row": 20,
        "rows": 15,
        "color": "blue",
        "start_x": -240,
        "start_y": 388,
        "stretch_len": 1,
    },
    "medium": {
        "width": 40,
        "height": 20,
        "padding": 5,
        "per_row": 16,
        "rows": 15,
        "color": "blue",
        "start_x": -228,
        "start_y": 388,
        "stretch_len": 2,
    },
    "large": {
        "width": 65,
        "height": 20,
        "padding": 6,
        "per_row": 7,
        "rows": 15,
        "color": "blue",
        "start_x": -216,
        "start_y": 388,
        "stretch_len": 3.25,
    },
}


class Brick(Turtle):
    def __init__(self, position, color, stretch_len):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=stretch_len, outline=None)
        self.penup()
        self.goto(position)

    def destroy(self):
        self.goto(1000, 1000)
        self.hideturtle()


def create_bricks(config):
    bricks = []
    width = config["width"]
    height = config["height"]
    padding = config["padding"]
    per_row = config["per_row"]
    rows = config["rows"]
    color = config["color"]
    start_x = config["start_x"]
    start_y = config["start_y"]
    stretch_len = config["stretch_len"]

    for row in range(rows):
        for column in range(per_row):
            x = start_x + (width + padding) * column
            y = start_y - (height + padding) * row
            brick = Brick((x, y), color, stretch_len)
            bricks.append(brick)
    return bricks
