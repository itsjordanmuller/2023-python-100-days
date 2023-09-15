from tkinter import *
from tkinter import ttk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class CategorySelector:
    def __init__(self, categories):
        self.window = Tk()
        self.window.title("Select Category")

        self.label = Label(
            self.window, text="Choose a category:", bg=THEME_COLOR, fg="white"
        )
        self.label.pack(pady=10)

        self.categories = categories
        self.category_name = StringVar()

        self.dropdown = ttk.Combobox(
            self.window,
            textvariable=self.category_name,
            values=["Any Category"] + list(categories.keys()),
        )
        self.dropdown.pack(pady=20)
        self.dropdown.set("Any Category")

        Button(self.window, text="Select", command=self.select_category).pack()

        self.window.mainloop()

    def select_category(self):
        if self.category_name.get() == "Any Category":
            self.selected_category_id = None
        else:
            self.selected_category_id = self.categories[self.category_name.get()]
        self.window.destroy()

    def get_category_id(self):
        return self.selected_category_id


class DifficultySelector:
    def __init__(self):
        self.window = Tk()
        self.window.title("Select Difficulty")

        self.difficulty = StringVar()
        self.difficulty.set("medium")

        options = ["easy", "medium", "hard"]
        for idx, option in enumerate(options):
            Radiobutton(
                self.window,
                text=option.capitalize(),
                variable=self.difficulty,
                value=option,
            ).pack(anchor=W)

        Button(self.window, text="Start", command=self.start_quiz).pack()

        self.window.mainloop()

    def start_quiz(self):
        self.selected_difficulty = self.difficulty.get()
        self.window.destroy()

    def get_difficulty(self):
        return self.selected_difficulty


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
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've reached the end of the quiz!\n\nYou got: {self.quiz.score}/{self.quiz.question_number} correct.",
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
