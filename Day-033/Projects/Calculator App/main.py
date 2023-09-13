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


# OPERATIONS
def handle_operation(operation_symbol):
    global current_input, full_calculation
    full_calculation.append(current_input)
    full_calculation.append(operation_symbol)
    current_input = ""
    update_display()


# CLEAR INPUTS
def handle_ac_button():
    global current_input, full_calculation
    current_input = ""
    full_calculation = []
    last_calc_canvas.delete("all")
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
        fill="white",
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
        fill="white",
    )


# ADJUST FONT SIZES DYNAMICALLY
def dynamic_font_size(display_text):
    size_mapping = {7: 32, 8: 28, 9: 24, 10: 20, 11: 18, 12: 16, 13: 14}
    default_size = 10

    for length, size in size_mapping.items():
        if len(display_text) <= length:
            return size
    return default_size


# BUTTON CREATION
def create_button(window, text, command, bg_color, grid_position):
    button = Button(text=text, command=command, bg=bg_color, borderwidth=0)
    button.grid(
        column=grid_position[0],
        row=grid_position[1],
        sticky="EW",
        columnspan=grid_position[2] if len(grid_position) > 2 else 1,
    )
    return button


# UI SETUP
# Layout inspired by Maciej on Dribbble:
# https://dribbble.com/shots/17536429-Calculator-DailyUI

window = Tk()
window.title("EasyCalc")
window.config(padx=25, pady=25, bg="#7f8c8d")


# CANVAS AREAS
last_calc_canvas = Canvas(width=200, height=75, highlightthickness=0, bg="#34495e")
last_calc_canvas.create_text(
    200 - CANVAS_PADDING,
    75 - CANVAS_PADDING,
    text="",
    anchor="se",
    font=("TkDefaultFont", 14),
    fill="white",
)
last_calc_canvas.grid(column=0, row=0, columnspan=4, rowspan=2)

result_canvas = Canvas(width=200, height=75, highlightthickness=0, bg="#2c3e50")
result_canvas.create_text(
    200 - CANVAS_PADDING,
    75 - CANVAS_PADDING,
    text="",
    anchor="se",
    font=("TkDefaultFont", 32),
    fill="white",
)
result_canvas.grid(column=0, row=2, columnspan=4, rowspan=2)


# OPERATION/SPECIAL BUTTONS
operation_buttons_config = {
    "⇱": ("#bdc3c7", (0, 5)),
    "√": ("#bdc3c7", (1, 5)),
    "^": ("#bdc3c7", (2, 5)),
    "!": ("#bdc3c7", (3, 5)),
    "AC": ("#2980b9", (0, 6), handle_ac_button),
    "±": ("#2980b9", (1, 6), handle_pos_neg_button),
    "%": ("#2980b9", (2, 6), lambda: handle_operation("%")),
    "÷": ("#3498db", (3, 6), lambda: handle_operation("/")),
    "x": ("#3498db", (3, 7), lambda: handle_operation("*")),
    "-": ("#3498db", (3, 8), lambda: handle_operation("-")),
    "+": ("#3498db", (3, 9), lambda: handle_operation("+")),
    ".": ("#2980b9", (1, 10), handle_dec_button),
    "=": ("#9b59b6", (2, 10, 2), handle_equal_button),
}

for symbol, config in operation_buttons_config.items():
    if len(config) == 2:
        create_button(window, symbol, None, config[0], config[1])
    else:
        create_button(window, symbol, config[2], config[0], config[1])

# NUMBER BUTTONS
for number in range(10):
    if number == 0:
        row = 10
        col = 0
    else:
        row = 9 - (number - 1) // 3
        col = (number - 1) % 3
    create_button(
        window, str(number), lambda n=number: number_clicked(n), "#bdc3c7", (col, row)
    )


# Handle Keyboard Inputs
def on_key_press(event):
    if event.char.isdigit():
        number_clicked(event.char)
    elif event.char == ".":
        handle_dec_button()
    elif event.char in ["+", "-", "*", "/", "%"]:
        operations = {
            "+": lambda: handle_operation("+"),
            "-": lambda: handle_operation("-"),
            "*": lambda: handle_operation("*"),
            "/": lambda: handle_operation("/"),
            "%": lambda: handle_operation("%"),
        }
        operations[event.char]()
    elif event.keysym == "Return":
        handle_equal_button()
    elif event.keysym == "Escape":
        handle_ac_button()


window.bind("<Key>", on_key_press)


window.mainloop()
