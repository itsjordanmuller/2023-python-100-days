from tkinter import *

# CONSTANTS
CANVAS_PADDING = 10

# VARIABLES
current_input = ""
full_calculation = []


# NUMBER TYPING
def number_clicked(number):
    global current_input
    current_input += str(number)
    update_display()


# CLEAR INPUTS
def handle_ac_button():
    global current_input, full_calculation
    current_input = ""
    full_calculation = []
    last_calc_canvas.delete("all")
    update_display()


# OPERATIONS


# PLUS BUTTON
def handle_plus_button():
    global current_input, full_calculation
    full_calculation.append(current_input)
    full_calculation.append("+")
    current_input = ""
    update_display()


# MINUS BUTTON
def handle_minus_button():
    global current_input, full_calculation
    full_calculation.append(current_input)
    full_calculation.append("-")
    current_input = ""
    update_display()


# MULTIPLY BUTTON
def handle_mul_button():
    global current_input, full_calculation
    full_calculation.append(current_input)
    full_calculation.append("*")
    current_input = ""
    update_display()


# DIVISION BUTTON
def handle_div_button():
    global current_input, full_calculation
    full_calculation.append(current_input)
    full_calculation.append("/")
    current_input = ""
    update_display()


# MODULUS BUTTON
def handle_mod_button():
    global current_input, full_calculation
    full_calculation.append(current_input)
    full_calculation.append("%")
    current_input = ""
    update_display()


# DECIMAL BUTTON
def handle_dec_button():
    global current_input

    if "." not in current_input:
        current_input += "."
        update_display()


# POSITIVE/NEGATIVE BUTTON
def handle_pos_neg_button():
    global current_input

    if not current_input:
        return

    if current_input[0] == "-":
        current_input = current_input[1:]
    else:
        current_input = "-" + current_input

    update_display()


# CALCULATE/EQUAL BUTTON FUNCTIONS
def handle_equal_button():
    global current_input, full_calculation

    full_calculation.append(current_input)

    calculation_str = "".join(full_calculation)
    calculation_str = calculation_str.replace("x", "*")

    try:
        result = eval(calculation_str)
        if isinstance(result, float):
            if result.is_integer():
                result = int(result)
            else:
                result = round(result, 10)
    except Exception as e:
        result = "Error"

    last_calc_display = calculation_str.replace("*", "x")
    last_calc_canvas.delete("all")
    last_calc_canvas.create_text(
        200 - CANVAS_PADDING,
        75 - CANVAS_PADDING,
        text=last_calc_display,
        anchor="se",
        font=("TkDefaultFont", 14),
    )

    full_calculation = []
    current_input = str(result)

    update_display()


# UPDATE DISPLAY
def update_display():
    global current_input, full_calculation
    display_text = "".join(full_calculation) + current_input
    display_text = display_text.replace("*", "x")
    font_size = dynamic_font_size(display_text)
    result_canvas.delete("all")
    result_canvas.create_text(
        200 - CANVAS_PADDING,
        75 - CANVAS_PADDING,
        text=display_text,
        anchor="se",
        font=("TkDefaultFont", font_size),
    )


# ADJUST FONT SIZES DYNAMICALLY
def dynamic_font_size(display_text):
    size_mapping = {7: 32, 8: 28, 9: 24, 10: 20, 11: 18, 12: 16, 13: 14}
    default_size = 10

    for length, size in size_mapping.items():
        if len(display_text) <= length:
            return size
    return default_size


# UI SETUP
# Layout inspired by Maciej on Dribbble:
# https://dribbble.com/shots/17536429-Calculator-DailyUI

window = Tk()
window.title("EasyCalc")
window.config(padx=25, pady=25)


# CANVAS AREAS
last_calc_canvas = Canvas(width=200, height=75, highlightthickness=0, bg="blue")
last_calc_canvas.create_text(
    200 - CANVAS_PADDING,
    75 - CANVAS_PADDING,
    text="3 x 9",
    anchor="se",
    font=("TkDefaultFont", 14),
)
last_calc_canvas.grid(column=0, row=0, columnspan=4, rowspan=2)

result_canvas = Canvas(width=200, height=75, highlightthickness=0, bg="red")
result_canvas.create_text(
    200 - CANVAS_PADDING,
    75 - CANVAS_PADDING,
    text="27",
    anchor="se",
    font=("TkDefaultFont", 32),
)
result_canvas.grid(column=0, row=2, columnspan=4, rowspan=2)


# OPERATION/SPECIAL BUTTONS
ac_button = Button(text="AC", width=2, command=handle_ac_button)
ac_button.grid(column=0, row=5, sticky="EW")

pos_neg_button = Button(text="±", width=2, command=handle_pos_neg_button)
pos_neg_button.grid(column=1, row=5, sticky="EW")

mod_button = Button(text="%", width=2, command=handle_mod_button)
mod_button.grid(column=2, row=5, sticky="EW")

div_button = Button(text="÷", width=2, command=handle_div_button)
div_button.grid(column=3, row=5, sticky="EW")

mul_button = Button(text="x", command=handle_mul_button)
mul_button.grid(column=3, row=6, sticky="EW")

minus_button = Button(text="-", command=handle_minus_button)
minus_button.grid(column=3, row=7, sticky="EW")

plus_button = Button(text="+", command=handle_plus_button)
plus_button.grid(column=3, row=8, sticky="EW")

dec_button = Button(text=".", command=handle_dec_button)
dec_button.grid(column=1, row=9, sticky="EW")

equal_button = Button(text="=", command=handle_equal_button)
equal_button.grid(column=2, row=9, columnspan=2, sticky="EW")


# NUMBER BUTTONS
zero_button = Button(text="0", command=lambda: number_clicked(0))
zero_button.grid(column=0, row=9, sticky="EW")

one_button = Button(text="1", command=lambda: number_clicked(1))
one_button.grid(column=0, row=8, sticky="EW")

two_button = Button(text="2", command=lambda: number_clicked(2))
two_button.grid(column=1, row=8, sticky="EW")

three_button = Button(text="3", command=lambda: number_clicked(3))
three_button.grid(column=2, row=8, sticky="EW")

four_button = Button(text="4", command=lambda: number_clicked(4))
four_button.grid(column=0, row=7, sticky="EW")

five_button = Button(text="5", command=lambda: number_clicked(5))
five_button.grid(column=1, row=7, sticky="EW")

six_button = Button(text="6", command=lambda: number_clicked(6))
six_button.grid(column=2, row=7, sticky="EW")

seven_button = Button(text="7", command=lambda: number_clicked(7))
seven_button.grid(column=0, row=6, sticky="EW")

eight_button = Button(text="8", command=lambda: number_clicked(8))
eight_button.grid(column=1, row=6, sticky="EW")

nine_button = Button(text="9", command=lambda: number_clicked(9))
nine_button.grid(column=2, row=6, sticky="EW")


window.mainloop()
