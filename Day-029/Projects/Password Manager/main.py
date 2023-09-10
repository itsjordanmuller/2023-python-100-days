from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# PASSWORD GENERATOR
letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def gen_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)
    # print(f"Your password is: {password}")

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# SAVE PASSWORD


def save_data():
    details = {
        "website": website_entry.get(),
        "email/username": user_email_entry.get(),
        "password": password_entry.get(),
    }

    missing_fields = [key for key, value in details.items() if not value]

    if missing_fields:
        if len(missing_fields) > 1:
            missing_fields_str = (
                ", ".join(missing_fields[:-1]) + " and " + missing_fields[-1]
            )
            messagebox.showerror(
                title="Missing Details",
                message=f"The {missing_fields_str} fields are missing. Please make sure to fill them out.",
            )
        elif "website" in missing_fields:
            messagebox.showerror(
                title="Missing Details", message="Please enter a website name/URL."
            )
        elif "email/username" in missing_fields:
            messagebox.showerror(
                title="Missing Details", message="Please enter a email/username."
            )
        elif "password" in missing_fields:
            messagebox.showerror(
                title="Missing Details", message="Please enter a password."
            )
    else:
        is_ok = messagebox.askokcancel(
            title=f"Save {details['website']} Password",
            message=f"Here's the login details:\n\nEmail: {details['email/username']}\nPassword: {details['password']}\n\nIs it okay to save?",
        )

        if is_ok:
            with open("login_data.txt", "a") as file:
                file.write(
                    f"{details['website']} | {details['email']} | {details['password']}\n"
                )

            website_entry.delete(0, END)
            password_entry.delete(0, END)


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
user_email_entry.insert(0, "itsjordanmuller@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky="E")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

gen_password_button = Button(text="Generate Password", pady=0, command=gen_password)
gen_password_button.grid(column=2, row=3, sticky="EW")

add_password_button = Button(text="Add", width=32, command=save_data)
add_password_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
