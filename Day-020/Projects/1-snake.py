from turtle import Turtle, Screen


def create_segment(x, y):
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(x, y)
    return segment


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

segments = []
for i in range(3):
    x_position = i * -20
    segment = create_segment(x_position, 0)
    segments.append(segment)

# segment_1 = Turtle("square")
# segment_1.color("white")
# segment_1.penup()

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.penup()
# segment_2.goto(x=-20, y=0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.penup()
# segment_3.goto(x=-40, y=0)

screen.exitonclick()
