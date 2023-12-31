from tkinter import *
import random


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")

        self.canvas_size = 128
        self.canvases = []

        self.canvas_states = {}

        self.x_score = 0
        self.o_score = 0
        self.round = 1

        self.score_canvas = Canvas(width=384, height=128)

        self.score_canvas.create_rectangle(28, 36, 100, 92, fill="red")

        self.score_canvas.create_rectangle(284, 36, 356, 92, fill="blue")

        self.score_canvas.create_rectangle(38, 46, 90, 82, fill="black")

        self.score_canvas.create_rectangle(294, 46, 346, 82, fill="black")

        self.score_canvas.create_text(
            64,
            64,
            text="99",
            font=("TkFixedFont", 20),
            justify="center",
            fill="white",
            tags="xScore",
        )

        self.score_canvas.create_text(
            320,
            64,
            text="99",
            font=("TkFixedFont", 20),
            justify="center",
            fill="white",
            tags="oScore",
        )

        self.score_canvas.create_text(
            64, 20, text="X", font=("TkFixedFont", 18), justify="center", fill="red"
        )

        self.score_canvas.create_text(
            320, 20, text="O", font=("TkFixedFont", 18), justify="center", fill="blue"
        )

        self.score_canvas.create_text(
            64, 104, text="(Left Click)", font=("TkFixedFont", 10), justify="center"
        )

        self.score_canvas.create_text(
            320, 104, text="(Right Click)", font=("TkFixedFont", 10), justify="center"
        )

        self.score_canvas.create_text(
            192, 48, text="Scores", font=("TkFixedFont", 24), justify="center"
        )

        self.score_canvas.create_text(
            192,
            80,
            text="Round: 1",
            font=("TkFixedFont", 16),
            justify="center",
            tags="round",
        )

        self.score_canvas.grid(row=0, column=0, columnspan=3, sticky="EW")

        self.turn_label = Label(text="X Goes", bg="red", font=("TkFixedFont", 24))
        self.turn_label.grid(row=4, column=0, columnspan=3)

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
                canvas.grid(row=i + 1, column=j)
                canvas.bind("<Button-1>", self.place_x)
                canvas.bind("<Button-3>", self.place_o)
                self.canvases.append(canvas)

                self.canvas_states[(i, j)] = "Empty"

        self.update_score_display()

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

            winner = self.check_win()
            if winner:
                self.end_game(winner)
            elif self.check_draw():
                self.end_draw_game()

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

            winner = self.check_win()
            if winner:
                self.end_game(winner)
            elif self.check_draw():
                self.end_draw_game()

    def update_turn(self):
        if self.current_turn == "X":
            self.turn_label.config(text="X Goes", bg="red")
            self.window.config(bg="red")
        else:
            self.turn_label.config(text="O Goes", bg="blue")
            self.window.config(bg="blue")

    def check_win(self):
        for i in range(3):
            # Check rows
            if (
                self.canvas_states[(i, 0)]
                == self.canvas_states[(i, 1)]
                == self.canvas_states[(i, 2)]
                and self.canvas_states[(i, 0)] != "Empty"
            ):
                return self.canvas_states[(i, 0)]

            # Check columns
            if (
                self.canvas_states[(0, i)]
                == self.canvas_states[(1, i)]
                == self.canvas_states[(2, i)]
                and self.canvas_states[(0, i)] != "Empty"
            ):
                return self.canvas_states[(0, i)]

        # Check diagonals
        if (
            self.canvas_states[(0, 0)]
            == self.canvas_states[(1, 1)]
            == self.canvas_states[(2, 2)]
            and self.canvas_states[(0, 0)] != "Empty"
        ):
            return self.canvas_states[(0, 0)]
        if (
            self.canvas_states[(0, 2)]
            == self.canvas_states[(1, 1)]
            == self.canvas_states[(2, 0)]
            and self.canvas_states[(0, 2)] != "Empty"
        ):
            return self.canvas_states[(0, 2)]

        return None

    def check_draw(self):
        return all(val != "Empty" for val in self.canvas_states.values())

    def end_draw_game(self):
        self.turn_label.config(text="Draw!", bg="yellow")
        self.window.config(bg="yellow")

        for canvas in self.canvases:
            canvas.unbind("<Button-1>")
            canvas.unbind("<Button-3>")

        self.create_next_round_button()
        self.check_game_over()

    def end_game(self, winner):
        self.turn_label.config(text=f"{winner} Wins!", bg="green")
        self.window.config(bg="green")

        if winner == "X":
            self.x_score += 1
        elif winner == "O":
            self.o_score += 1
        self.update_score_display()

        for canvas in self.canvases:
            canvas.unbind("<Button-1>")
            canvas.unbind("<Button-3>")

        self.create_next_round_button()
        self.check_game_over()

    def create_next_round_button(self):
        self.next_round_button = Button(
            self.window,
            text="Next Round",
            command=self.reset_game,
            font=("TkFixedFont", 24),
        )
        self.next_round_button.grid(row=5, column=0, columnspan=3, sticky="EW")

    def reset_game(self):
        for i, j in self.canvas_states:
            self.canvas_states[(i, j)] = "Empty"
        for canvas in self.canvases:
            canvas.delete("all")
            canvas.configure(bg="white")
            canvas.bind("<Button-1>", self.place_x)
            canvas.bind("<Button-3>", self.place_o)
        self.current_turn = random.choice(["X", "O"])
        self.update_turn()
        self.round += 1
        self.update_round_display()
        self.next_round_button.grid_forget()

    def update_score_display(self):
        self.score_canvas.delete("xScore")
        self.score_canvas.delete("oScore")
        self.score_canvas.create_text(
            64,
            64,
            text=str(self.x_score),
            font=("TkFixedFont", 20),
            justify="center",
            fill="white",
            tags="xScore",
        )
        self.score_canvas.create_text(
            320,
            64,
            text=str(self.o_score),
            font=("TkFixedFont", 20),
            justify="center",
            fill="white",
            tags="oScore",
        )

    def update_round_display(self):
        self.score_canvas.delete("round")
        self.score_canvas.create_text(
            192,
            80,
            text=f"Round: {self.round}",
            font=("TkFixedFont", 16),
            justify="center",
            tags="round",
        )

    def check_game_over(self):
        if self.x_score + self.o_score == 3:
            if self.x_score == 2:
                self.end_whole_game("X")
            elif self.o_score == 2:
                self.end_whole_game("O")

    def end_whole_game(self, winner):
        self.turn_label.config(text=f"{winner} Wins!", bg="green")
        self.window.config(bg="green")
        for canvas in self.canvases:
            canvas.unbind("<Button-1>")
            canvas.unbind("<Button-3>")
        self.next_round_button.config(text="Restart Game", command=self.restart_game)

    def restart_game(self):
        self.x_score = 0
        self.o_score = 0
        self.round = 1
        self.update_score_display()
        self.update_round_display()
        for i, j in self.canvas_states:
            self.canvas_states[(i, j)] = "Empty"
        for canvas in self.canvases:
            canvas.delete("all")
            canvas.configure(bg="white")
            canvas.bind("<Button-1>", self.place_x)
            canvas.bind("<Button-3>", self.place_o)
        self.current_turn = random.choice(["X", "O"])
        self.update_turn()
        self.next_round_button.grid_forget()
