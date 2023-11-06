from turtle import Turtle

# SMALL BRICKS
# BRICK_WIDTH = 20
# BRICK_HEIGHT = 20
# BRICK_PADDING = 5
# BRICKS_PER_ROW = 20
# NUMBER_OF_ROWS = 15
# BRICK_COLOR = "blue"
# START_X = -240
# START_Y = 440
# STRETCH_LEN = 1

# MEDIUM BRICKS
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICK_PADDING = 5
BRICKS_PER_ROW = 16
NUMBER_OF_ROWS = 15
BRICK_COLOR = "blue"
START_X = -230
START_Y = 440
STRETCH_LEN = 2

# BIG BRICKS
# BRICK_WIDTH = 60
# BRICK_HEIGHT = 20
# BRICK_PADDING = 9
# BRICKS_PER_ROW = 7
# NUMBER_OF_ROWS = 15
# BRICK_COLOR = "blue"
# START_X = -210
# START_Y = 430
# STRETCH_LEN = 3


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(BRICK_COLOR)
        self.shapesize(stretch_wid=1, stretch_len=STRETCH_LEN, outline=None)
        self.penup()
        self.goto(position)


def create_bricks():
    bricks = []
    for row in range(NUMBER_OF_ROWS):
        for column in range(BRICKS_PER_ROW):
            x = START_X + (BRICK_WIDTH + BRICK_PADDING) * column
            y = START_Y - (BRICK_HEIGHT + BRICK_PADDING) * row
            brick = Brick((x, y))
            bricks.append(brick)
    return bricks
