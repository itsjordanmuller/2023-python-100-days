from tkinter import *
import random


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")

        self.canvas_size = 128
        self.canvases = []

        self.canvas_states = {}

        self.turn_label = Label(text="X Goes", bg="red", font=("TkFixedFont", 24))
        self.turn_label.grid(row=3, column=0, columnspan=3)

        self.current_turn = random.choice(["X", "O"])
        self.update_turn()

        self.x_img = PhotoImage(file="./images/x.png").subsample(5, 5)
        self.o_img = PhotoImage(file="./images/o.png").subsample(5, 5)

        for i in range(3):
            for j in range(3):
                canvas = Canvas(
                    self.window,
                    width=self.canvas_size,
                    height=self.canvas_size,
                    bg="white",
                )
                canvas.grid(row=i, column=j)
                canvas.bind("<Button-1>", self.place_x)
                canvas.bind("<Button-3>", self.place_o)
                self.canvases.append(canvas)

                self.canvas_states[(i, j)] = "Empty"

        self.window.mainloop()

    def get_canvas_position(self, canvas):
        return next(
            (
                position
                for position, c in zip(self.canvas_states.keys(), self.canvases)
                if c == canvas
            ),
            None,
        )

    def place_x(self, event):
        canvas = event.widget
        position = self.get_canvas_position(canvas)

        if (
            position
            and self.current_turn == "X"
            and self.canvas_states[position] == "Empty"
        ):
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()

            canvas.create_image(canvas_width // 2, canvas_height // 2, image=self.x_img)
            canvas.configure(bg="red")

            self.canvas_states[position] = "X"
            self.current_turn = "O"
            self.update_turn()

    def place_o(self, event):
        canvas = event.widget
        position = self.get_canvas_position(canvas)

        if (
            position
            and self.current_turn == "O"
            and self.canvas_states[position] == "Empty"
        ):
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()

            canvas.create_image(canvas_width // 2, canvas_height // 2, image=self.o_img)
            canvas.configure(bg="blue")

            self.canvas_states[position] = "O"
            self.current_turn = "X"
            self.update_turn()

    def update_turn(self):
        self.print_canvas_states()
        if self.current_turn == "X":
            self.turn_label.config(text="X Goes", bg="red")
            self.window.config(bg="red")
        else:
            self.turn_label.config(text="O Goes", bg="blue")
            self.window.config(bg="blue")
