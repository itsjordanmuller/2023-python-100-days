from tkinter import *

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
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
window.config(padx=100, pady=50, bg="#ffebcd")

canvas = Canvas(width=200, height=224, bg="#ffebcd", highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
canvas.create_text(100, 140, text="00:00", font=(FONT_NAME, 26, "bold"), fill="white")
canvas.pack(expand=True)

window.mainloop()
