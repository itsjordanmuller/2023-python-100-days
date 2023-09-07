from tkinter import *


i = 0


def button_clicked():
    global i
    print("Button was clicked!")
    i += 1
    my_label["text"] = f"Button Clicked {i} Times!"


def input_label():
    input_value = input.get()
    my_label["text"] = input_value


# Window
window = Tk()
window.title("Python GUI Program")
window.minsize(width=500, height=400)

# Label
my_label = Label(text="I am a label!", font=("Arial", 24, "bold"))
my_label["text"] = "New Label Text!"
my_label.pack(side="left")

# Button
button = Button(text="Button!", command=input_label)
button.pack(side="left")

# Entry
input = Entry(width=10)
input.pack(side="left")


window.mainloop()
