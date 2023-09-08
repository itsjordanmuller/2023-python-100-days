from tkinter import *

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#097969"
TAN = "#ffebcd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# TIMER RESET

# TIMER MECHANISM

# COUNTDOWN MECHANISM

# UI SETUP
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=TAN)

timer_label = Label(text="Timer")
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=TAN, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
canvas.create_text(100, 140, text="00:00", font=(FONT_NAME, 26, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start")
start_button.grid(column=0, row=2)

reset_button = Button(text="Start")
reset_button.grid(column=2, row=2)

check_label = Label(text="✓")
check_label.grid(column=1, row=3)

window.mainloop()
