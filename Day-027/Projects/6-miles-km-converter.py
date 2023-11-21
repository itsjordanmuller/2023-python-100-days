from tkinter import *


# Conversion function
def convert():
    # Convert from miles to kilometers
    if mode.get() == "Miles to Km":
        miles = float(miles_input.get())
        kilometers = miles * 1.60934
        result_label["text"] = f"{kilometers:.4f}"
    # Convert from kilometers to miles
    else:
        kilometers = float(miles_input.get())
        miles = kilometers / 1.60934
        result_label["text"] = f"{miles:.4f}"


# Toggle between conversion modes
def toggle_conversion():
    # Switch to Km to Miles mode
    if mode.get() == "Miles to Km":
        mode.set("Km to Miles")
        input_label.config(text="Km")
        result_unit_label.config(text="Miles")
    # Switch to Miles to Km mode
    else:
        mode.set("Miles to Km")
        input_label.config(text="Miles")
        result_unit_label.config(text="Km")
    # Reset input and result fields
    result_label["text"] = "0"
    miles_input.delete(0, END)
    miles_input.insert(END, string="0")


# Set up GUI
window = Tk()
window.title("Unit Converter")
window.config(padx=30, pady=30)

mode = StringVar(value="Miles to Km")

# Input field for distance
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0, padx=5, pady=5)

# Label for input unit
input_label = Label(text="Miles")
input_label.grid(column=2, row=0, padx=5, pady=5)

# Label for conversion equality
equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1, padx=5, pady=5)

# Label for conversion result
result_label = Label(text="0")
result_label.grid(column=1, row=1, padx=5, pady=5)

# Label for result unit
result_unit_label = Label(text="Km")
result_unit_label.grid(column=2, row=1, padx=5, pady=5)

# Button for triggering conversion
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

# Button for toggling conversion mode
toggle_button = Button(text="Toggle Conversion", command=toggle_conversion)
toggle_button.grid(column=1, row=3)

window.mainloop()
