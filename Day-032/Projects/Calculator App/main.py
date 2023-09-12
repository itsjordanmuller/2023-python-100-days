from tkinter import *

# UI SETUP
window = Tk()
window.title("EasyCalc")
window.config(padx=50, pady=50)

last_calc_canvas = Canvas(width=200, height=75, highlightthickness=0, bg="blue")
last_calc_canvas.grid(column=0, row=0, columnspan=4, rowspan=2)

result_canvas = Canvas(width=200, height=75, highlightthickness=0, bg="red")
result_canvas.grid(column=0, row=2, columnspan=4, rowspan=2)

ac_button = Button(text="AC")
ac_button.grid(column=0, row=5, sticky="EW")

pos_neg_button = Button(text="±")
pos_neg_button.grid(column=1, row=5, sticky="EW")

mod_button = Button(text="%")
mod_button.grid(column=2, row=5, sticky="EW")

div_button = Button(text="÷")
div_button.grid(column=3, row=5, sticky="EW")

mul_button = Button(text="x")
mul_button.grid(column=3, row=6, sticky="EW")

minus_button = Button(text="-")
minus_button.grid(column=3, row=7, sticky="EW")

plus_button = Button(text="+")
plus_button.grid(column=3, row=8, sticky="EW")

comma_button = Button(text=",")
comma_button.grid(column=1, row=9, sticky="EW")

equal_button = Button(text="=")
equal_button.grid(column=2, row=9, columnspan=2, sticky="EW")


window.mainloop()
