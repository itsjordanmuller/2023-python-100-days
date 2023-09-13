from tkinter import *
import math

# CONSTANTS
CANVAS_PADDING = 10
WINDOW_COLOR = "#7f8c8d"
TOP_CANVAS_COLOR = "#34495e"
BOTTOM_CANVAS_COLOR = "#2c3e50"
NORMAL_BUTTON_COLOR = "#bdc3c7"


# THEMES
THEMES = {
    "blue_purple": {
        "DARK_COLOR": "#2980b9",
        "LIGHT_COLOR": "#3498db",
        "ACCENT_COLOR": "#9b59b6",
    },
    "red_orange": {
        "DARK_COLOR": "#b33939",
        "LIGHT_COLOR": "#ff5252",
        "ACCENT_COLOR": "#ff793f",
    },
    "green_blue": {
        "DARK_COLOR": "#218c74",
        "LIGHT_COLOR": "#33d9b2",
        "ACCENT_COLOR": "#706fd3",
    },
}

current_theme = "red_orange"


def apply_theme(theme_name):
    global DARK_COLOR, LIGHT_COLOR, ACCENT_COLOR

    if theme_name in THEMES:
        theme = THEMES[theme_name]
        DARK_COLOR = theme["DARK_COLOR"]
        LIGHT_COLOR = theme["LIGHT_COLOR"]
        ACCENT_COLOR = theme["ACCENT_COLOR"]
    else:
        DARK_COLOR = "#2c3e50"
        LIGHT_COLOR = "#34495e"
        ACCENT_COLOR = "#7f8c8d"


apply_theme(current_theme)

theme_names = list(THEMES.keys())

theme_index = theme_names.index(current_theme)


def cycle_theme():
    global theme_index, DARK_COLOR, LIGHT_COLOR, ACCENT_COLOR
    theme_index = (theme_index + 1) % len(theme_names)

    apply_theme(theme_names[theme_index])

    for symbol, config in operation_buttons_config.items():
        if symbol in ["AC", "±", "%"]:
            config_color = DARK_COLOR
        elif symbol in ["÷", "x", "-", "+"]:
            config_color = LIGHT_COLOR
        elif symbol == "=":
            config_color = ACCENT_COLOR
        else:
            config_color = NORMAL_BUTTON_COLOR

        if symbol in button_objects:
            button_objects[symbol].config(bg=config_color)


# VARIABLES
current_input = ""
full_calculation = []
button_objects = {}
is_expanded = False


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

# EXPAND BUTTON
def handle_expand_button():
    global is_expanded
    new_width = 400 if not is_expanded else 200
    last_calc_canvas.config(width=new_width)
    result_canvas.config(width=new_width)
    is_expanded = not is_expanded


# SQUARE ROOT BUTTON
def handle_sqrt_button():
    global current_input
    try:
        current_input = str(math.sqrt(float(current_input)))
        update_display()
    except ValueError:
        current_input = "Error"
        update_display()


# EXPONENT BUTTON
def handle_exp_button():
    global current_input
    if current_input:
        current_input += "**2"
        handle_equal_button()


# FACTORIAL BUTTON
def handle_fact_button():
    global current_input
    try:
        current_input = str(math.factorial(int(current_input)))
        update_display()
    except (ValueError, OverflowError):
        current_input = "Error"
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

    button_objects[text] = button

    return button


# UI SETUP
# Layout inspired by Maciej on Dribbble:
# https://dribbble.com/shots/17536429-Calculator-DailyUI

window = Tk()
window.title("EasyCalc")
window.config(padx=25, pady=25, bg=WINDOW_COLOR)


# CANVAS AREAS
last_calc_canvas = Canvas(
    width=200, height=75, highlightthickness=0, bg=TOP_CANVAS_COLOR
)
last_calc_canvas.create_text(
    200 - CANVAS_PADDING,
    75 - CANVAS_PADDING,
    text="",
    anchor="se",
    font=("TkDefaultFont", 14),
    fill="white",
)
last_calc_canvas.grid(column=0, row=0, columnspan=4, rowspan=2)

result_canvas = Canvas(
    width=200, height=75, highlightthickness=0, bg=BOTTOM_CANVAS_COLOR
)
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
    "⇱": (NORMAL_BUTTON_COLOR, (0, 5), handle_expand_button),
    "√": (NORMAL_BUTTON_COLOR, (1, 5), handle_sqrt_button),
    "^": (NORMAL_BUTTON_COLOR, (2, 5), handle_exp_button),
    "!": (NORMAL_BUTTON_COLOR, (3, 5), handle_fact_button),
    "AC": (DARK_COLOR, (0, 6), handle_ac_button),
    "±": (DARK_COLOR, (1, 6), handle_pos_neg_button),
    "%": (DARK_COLOR, (2, 6), lambda: handle_operation("%")),
    "÷": (LIGHT_COLOR, (3, 6), lambda: handle_operation("/")),
    "x": (LIGHT_COLOR, (3, 7), lambda: handle_operation("*")),
    "-": (LIGHT_COLOR, (3, 8), lambda: handle_operation("-")),
    "+": (LIGHT_COLOR, (3, 9), lambda: handle_operation("+")),
    ".": (DARK_COLOR, (1, 10), handle_dec_button),
    "=": (ACCENT_COLOR, (2, 10, 2), handle_equal_button),
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
        window,
        str(number),
        lambda n=number: number_clicked(n),
        NORMAL_BUTTON_COLOR,
        (col, row),
    )


# Handle Keyboard Inputs
def on_key_press(event):
    if event.char.isdigit():
        number_clicked(event.char)
    elif event.char.upper() == "T":
        cycle_theme()
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
