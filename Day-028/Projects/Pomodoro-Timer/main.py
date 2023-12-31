from tkinter import *
import math

# Constants for UI color and timer settings
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379b46"
TAN = "#ffebcd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Timer variables
reps = 0
marks = ""
timer = None


# Countdown mechanism
def timer_countdown(count):
    global timer

    # Convert count to mm:ss format
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"

    # Update timer display
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    # Recursive countdown or start next timer phase
    if count > 0:
        timer = window.after(1000, timer_countdown, count - 1)
    else:
        start_timer()


# Timer control
def start_timer():
    global reps, marks

    # Update timer for work or break phases
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    # Determine current phase and set countdown
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=GREEN)
        timer_countdown(long_break_seconds)
        marks += "✓\n"
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        timer_countdown(short_break_seconds)
        marks += "✓"
    else:
        timer_label.config(text="Work", fg=RED)
        timer_countdown(work_seconds)

    # Update marks
    check_label.config(text=marks)


# Reset timer
def reset_timer():
    global reps, marks, timer

    # Cancel current timer and reset variables
    window.after_cancel(timer)
    reps = 0
    marks = ""

    # Reset UI elements to default state
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")


# UI setup
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=TAN)

# Timer label
timer_label = Label(text="Timer", bg=TAN, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

# Timer display
canvas = Canvas(width=200, height=224, bg=TAN, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(
    100, 140, text="00:00", font=(FONT_NAME, 26, "bold"), fill="white"
)
canvas.grid(column=1, row=1, padx=20, pady=10)

# Control buttons
start_button = Button(text="Start", bg="white", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", bg="white", command=reset_timer)
reset_button.grid(column=2, row=2)

# Progress marks label
check_label = Label(text="", bg=TAN, fg=GREEN, font=(FONT_NAME, 18, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
