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
window.config(padx=50, pady=50)

# Label
my_label = Label(text="I am a label!", font=("Arial", 24, "bold"))
my_label["text"] = "New Label Text!"
# my_label.pack(side="left")
# my_label.place(
#     x=10,
#     y=10,
# )
my_label.config(padx=50, pady=50)
my_label.grid(column=0, row=0)

# Button
button = Button(text="Button!", command=input_label)
# button.pack(side="left")
button.grid(column=1, row=1)

new_button = Button(text="New Button!", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
# input.pack(side="left")
input.grid(column=3, row=2)


window.mainloop()
