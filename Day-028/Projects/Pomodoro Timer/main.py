from tkinter import *
import math

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379b46"
TAN = "#ffebcd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0

# TIMER RESET

# TIMER MECHANISM

# COUNTDOWN MECHANISM


def timer_countdown(count):
    # print(count)

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        window.after(1000, timer_countdown, count - 1)


def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_countdown(long_break_seconds)
    elif reps % 2 == 0:
        timer_countdown(short_break_seconds)
    else:
        timer_countdown(work_seconds)

    # timer_countdown(5 * 60)


# UI SETUP
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=TAN)

timer_label = Label(text="Timer", bg=TAN, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=TAN, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(
    100, 140, text="00:00", font=(FONT_NAME, 26, "bold"), fill="white"
)
canvas.grid(column=1, row=1, padx=20, pady=10)

start_button = Button(text="Start", bg="white", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="white")
reset_button.grid(column=2, row=2)

check_label = Label(text="✓", bg=TAN, fg=GREEN, font=(FONT_NAME, 18, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
