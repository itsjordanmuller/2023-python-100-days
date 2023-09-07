from tkinter import *


def miles_to_km():
    miles = miles_input.get()
    kilometers = int(miles) * 1.60934
    km_result_label["text"] = f"{kilometers}"
    return kilometers


window = Tk()
window.title("Unit Converter (miles to km)")
window.config(padx=30, pady=30)

miles_input = Entry()
miles_input.config(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0, padx=5, pady=5)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0, padx=5, pady=5)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1, padx=5, pady=5)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1, padx=5, pady=5)

km_label = Label(text="km")
km_label.grid(column=2, row=1, padx=10, pady=10)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
