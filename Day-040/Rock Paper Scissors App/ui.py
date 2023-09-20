from tkinter import *
from game import Game


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Rock Paper Scissors")
        self.game = Game()

        # Paper icons created by Freepik - Flaticon
        # https://www.flaticon.com/free-icons/paper
        self.paper_img = PhotoImage(file="./images/scroll.png").subsample(6, 6)

        # Rock icons created by Freepik - Flaticon
        # https://www.flaticon.com/free-icons/rock
        self.rock_img = PhotoImage(file="./images/stone.png").subsample(5, 5)

        # Scissors icons created by Freepik - Flaticon
        # https://www.flaticon.com/free-icons/scissors
        self.scissors_img = PhotoImage(file="./images/scissors.png").subsample(6, 6)

        self.score_canvas = Canvas(
            self.window,
            width=448,
            height=64,
            highlightthickness=0,
            borderwidth=0,
            bg="red",
        )

        self.score_canvas.create_rectangle(
            0,
            0,
            96,
            64,
            fill="black",
            width=0,
        )

        self.score_canvas.create_rectangle(
            352,
            0,
            448,
            64,
            fill="black",
            width=0,
        )

        self.score_canvas.create_rectangle(
            20,
            16,
            76,
            48,
            fill="white",
            width=0,
        )

        self.score_canvas.create_rectangle(
            372,
            16,
            428,
            48,
            fill="white",
            width=0,
        )

        self.score_canvas.create_text(
            142,
            32,
            font=("TkFixedFont", 16),
            text="Player",
            justify="center",
            fill="black",
        )

        self.score_canvas.create_text(
            286,
            32,
            font=("TkFixedFont", 16),
            text="Computer",
            justify="center",
            fill="black",
        )

        self.player_score_text = self.score_canvas.create_text(
            48,
            32,
            font=("TkFixedFont", 16),
            text="0",
            justify="center",
            fill="black",
        )

        self.computer_score_text = self.score_canvas.create_text(
            400,
            32,
            font=("TkFixedFont", 16),
            text="0",
            justify="center",
            fill="black",
        )

        self.score_canvas.grid(column=0, row=0, columnspan=3)

        self.game_canvas = Canvas(
            self.window,
            width=448,
            height=448,
            highlightthickness=0,
            borderwidth=0,
            bg="orange",
        )
        self.game_canvas.grid(column=0, row=1, columnspan=3)

        self.button_canvas = Canvas(
            self.window,
            width=448,
            height=192,
            highlightthickness=0,
            borderwidth=0,
            bg="#2c3e50",
        )

        self.rock_button = Button(
            self.button_canvas,
            image=self.rock_img,
            borderwidth=0,
            highlightthickness=0,
            relief=FLAT,
            bg="#2c3e50",
            activebackground="#2c3e50",
        )
        self.button_canvas.create_window(84, 80, window=self.rock_button)

        self.paper_button = Button(
            self.button_canvas,
            image=self.paper_img,
            borderwidth=0,
            highlightthickness=0,
            relief=FLAT,
            bg="#2c3e50",
            activebackground="#2c3e50",
        )
        self.button_canvas.create_window(224, 80, window=self.paper_button)

        self.scissors_button = Button(
            self.button_canvas,
            image=self.scissors_img,
            borderwidth=0,
            highlightthickness=0,
            relief=FLAT,
            bg="#2c3e50",
            activebackground="#2c3e50",
        )
        self.button_canvas.create_window(364, 80, window=self.scissors_button)

        self.rock_text = self.button_canvas.create_text(
            84,
            152,
            font=("TkFixedFont", 16),
            text="Rock",
            justify="center",
            fill="white",
        )

        self.paper_text = self.button_canvas.create_text(
            224,
            152,
            font=("TkFixedFont", 16),
            text="Paper",
            justify="center",
            fill="white",
        )

        self.scissors_text = self.button_canvas.create_text(
            364,
            152,
            font=("TkFixedFont", 16),
            text="Scissors",
            justify="center",
            fill="white",
        )

        self.rock_button.bind(
            "<Enter>",
            lambda e: self.button_canvas.itemconfig(self.rock_text, fill="#f1c40f"),
        )
        self.paper_button.bind(
            "<Enter>",
            lambda e: self.button_canvas.itemconfig(self.paper_text, fill="#f1c40f"),
        )
        self.scissors_button.bind(
            "<Enter>",
            lambda e: self.button_canvas.itemconfig(self.scissors_text, fill="#f1c40f"),
        )

        self.rock_button.bind(
            "<Leave>",
            lambda e: self.button_canvas.itemconfig(self.rock_text, fill="white"),
        )
        self.paper_button.bind(
            "<Leave>",
            lambda e: self.button_canvas.itemconfig(self.paper_text, fill="white"),
        )
        self.scissors_button.bind(
            "<Leave>",
            lambda e: self.button_canvas.itemconfig(self.scissors_text, fill="white"),
        )

        self.rock_button["command"] = lambda: self.make_player_move("rock")

        self.paper_button["command"] = lambda: self.make_player_move("paper")

        self.scissors_button["command"] = lambda: self.make_player_move("scissors")

        self.button_canvas.grid(column=0, row=2, columnspan=3)

        self.window.mainloop()

    def make_player_move(self, choice):
        result, player_choice, computer_choice = self.game.player_move(choice)
        self.update_game_canvas(player_choice, computer_choice, result)
        self.update_score_canvas()

    def update_game_canvas(self, player_choice, computer_choice, result):
        self.game_canvas.delete("all")

        self.game_canvas.create_text(
            224,
            128,
            font=("TkFixedFont", 20),
            text=f"Player: {player_choice}",
            justify="center",
            fill="black",
        )

        self.game_canvas.create_text(
            224,
            196,
            font=("TkFixedFont", 20),
            text=f"Computer: {computer_choice}",
            justify="center",
            fill="black",
        )

        self.game_canvas.create_text(
            224,
            320,
            font=("TkFixedFont", 20),
            text=f"Result: {result}",
            justify="center",
            fill="black",
        )

    def update_score_canvas(self):
        player_score, computer_score = self.game.get_scores()
        self.score_canvas.itemconfig(self.player_score_text, text=str(player_score))
        self.score_canvas.itemconfig(self.computer_score_text, text=str(computer_score))
