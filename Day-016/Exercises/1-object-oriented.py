# from turtle import Turtle, Screen

# import tkinter as TK
# import another_module

# print(another_module.another_variable)
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ("Pikachu", "Squirtle", "Charmander"))
table.add_column("Type", ("Electric", "Water", "Fire"))
print(table)
