from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)

        self.score_label = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12)
        )
        self.score_label.grid(column=1, row=0, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            font=("Arial", 15, "italic"),
            width=260,
            justify="center",
        )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(
            self.window,
            image=self.true_image,
            borderwidth=0,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=self.true_pressed,
        )
        self.true_button.grid(column=0, row=2, pady=20, padx=20, sticky="E")

        self.false_button = Button(
            self.window,
            image=self.false_image,
            borderwidth=0,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=self.false_pressed,
        )
        self.false_button.grid(column=1, row=2, pady=20, padx=20, sticky="W")

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.quiz.check_answer("True")

    def false_pressed(self):
        self.quiz.check_answer("False")
