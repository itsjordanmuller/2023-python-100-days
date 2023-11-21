import json
import random
import pyperclip
from tkinter import *
from tkinter import messagebox


# LETTERS, NUMBERS & SYMBOLS FOR PASSWORD GENERATOR
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
    """Randomly determine the number of letters, symbols, and numbers"""
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

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


# READ PASSWORD
def read_data():
    """Read password data from JSON file"""
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="Error reading the data file.")


# SEARCH PASSWORD
def search_data():
    """Search for password by website name"""
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website in data:
                email = data[website]["email/username"]
                password = data[website]["password"]
                messagebox.showinfo(
                    title=website,
                    message=f"Email/Username: {email}\nPassword: {password}",
                )
            else:
                messagebox.showerror(
                    title="Error",
                    message=f"No details for the website {website} found.",
                )
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="Error reading the data file.")


# SAVE PASSWORD
def save_data():
    """Save new password details to JSON file"""
    details = {
        "website": website_entry.get(),
        "email/username": user_email_entry.get(),
        "password": password_entry.get(),
    }
    new_data = {
        details["website"]: {
            "email/username": details["email/username"],
            "password": details["password"],
        }
    }

    # Validate required fields
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
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}

        data.update(new_data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

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
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

search_button = Button(text="Search", pady=0, command=search_data)
search_button.grid(column=2, row=1, sticky="EW")

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
