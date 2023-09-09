from tkinter import *

# PASSWORD GENERATOR

# SAVE PASSWORD

# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=img)
canvas.pack(expand=True, padx=20, pady=20)


window.mainloop()
