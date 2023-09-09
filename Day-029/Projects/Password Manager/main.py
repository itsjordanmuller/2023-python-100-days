from tkinter import *

# PASSWORD GENERATOR

# SAVE PASSWORD

# UI SETUP
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky="E")

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

user_email_label = Label(text="Email/Username:")
user_email_label.grid(column=0, row=2, sticky="E")

user_email_entry = Entry()
user_email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="E")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

gen_password_button = Button(text="Generate Password", pady=0)
gen_password_button.grid(column=2, row=3, sticky="EW")

add_password_button = Button(text="Add", width=32)
add_password_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
