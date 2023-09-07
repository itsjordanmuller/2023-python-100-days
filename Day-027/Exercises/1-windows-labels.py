from tkinter import *

window = Tk()
window.title("Python GUI Program")
window.minsize(width=500, height=400)

my_label = Label(text="I am a label!", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Label Text!"
my_label.config(text="Yet Another Label!")

i = 0


def button_clicked():
    global i
    print("Button was clicked!")
    i += 1
    my_label["text"] = f"Button Clicked {i} Times!"


button = Button(text="Button!", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()


window.mainloop()
