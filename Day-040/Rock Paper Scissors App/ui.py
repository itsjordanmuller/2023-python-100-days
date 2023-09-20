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

        # Rock paper scissors icons created by Freepik - Flaticon
        # https://www.flaticon.com/free-icons/rock-paper-scissors
        self.game_img = PhotoImage(file="./images/rock-paper-scissors.png").subsample(
            2, 2
        )

        self.score_canvas = Canvas(
            self.window,
            width=448,
            height=64,
            highlightthickness=0,
            borderwidth=0,
            bg="#74b9ff",
        )

        self.score_canvas.create_rectangle(
            0,
            0,
            96,
            64,
            fill="#b2bec3",
            width=0,
        )

        self.score_canvas.create_rectangle(
            352,
            0,
            448,
            64,
            fill="#b2bec3",
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
            bg="#34495e",
        )

        self.game_canvas.create_image(224, 152, image=self.game_img, anchor=CENTER)

        self.game_canvas.create_text(
            224,
            352,
            font=("TkFixedFont", 28),
            text="Click a\nButton Below!",
            fill="white",
            justify="center",
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

        self.choice_images = {
            "rock": self.rock_img,
            "paper": self.paper_img,
            "scissors": self.scissors_img,
        }

        self.window.mainloop()

    def make_player_move(self, choice):
        result, player_choice, computer_choice = self.game.player_move(choice)
        self.update_game_canvas(player_choice, computer_choice, result)
        self.update_score_canvas()

    def round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1 + radius,
            y1,
            x1 + radius,
            y1,
            x2 - radius,
            y1,
            x2 - radius,
            y1,
            x2,
            y1,
            x2,
            y1 + radius,
            x2,
            y1 + radius,
            x2,
            y2 - radius,
            x2,
            y2 - radius,
            x2,
            y2,
            x2 - radius,
            y2,
            x2 - radius,
            y2,
            x1 + radius,
            y2,
            x1 + radius,
            y2,
            x1,
            y2,
            x1,
            y2 - radius,
            x1,
            y2 - radius,
            x1,
            y1 + radius,
            x1,
            y1 + radius,
            x1,
            y1,
        ]

        return self.game_canvas.create_polygon(points, **kwargs, smooth=True)

    def update_game_canvas(self, player_choice, computer_choice, result):
        self.game_canvas.delete("all")
        self.round_rectangle(32, 32, 416, 260, radius=25, fill="#74b9ff")
        self.round_rectangle(40, 296, 404, 424, radius=25, fill="#b2bec3")
        self.round_rectangle(60, 316, 384, 404, radius=25, fill="white")

        circle_radius = 60
        if result == "player":
            self.game_canvas.create_oval(
                112 - circle_radius,
                114 - circle_radius,
                112 + circle_radius,
                114 + circle_radius,
                outline="black",
                fill="#c4e538",
                width=3,
            )
        elif result == "computer":
            self.game_canvas.create_oval(
                336 - circle_radius,
                114 - circle_radius,
                336 + circle_radius,
                114 + circle_radius,
                outline="black",
                fill="#c4e538",
                width=3,
            )

        player_image = self.choice_images[player_choice]
        self.game_canvas.create_image(112, 114, image=player_image, anchor=CENTER)

        computer_image = self.choice_images[computer_choice]
        self.game_canvas.create_image(336, 114, image=computer_image, anchor=CENTER)

        result_string = self.generate_result_string(
            player_choice, computer_choice, result
        )

        self.game_canvas.create_text(
            112,
            214,
            font=("TkFixedFont", 14),
            text="Player\nChoice",
            justify="center",
            fill="black",
        )

        self.game_canvas.create_text(
            336,
            214,
            font=("TkFixedFont", 14),
            text="Computer\nChoice",
            justify="center",
            fill="black",
        )

        self.game_canvas.create_text(
            224,
            114,
            font=("TkFixedFont", 18),
            text="vs.",
            justify="center",
            fill="black",
        )

        self.game_canvas.create_text(
            224,
            360,
            font=("TkFixedFont", 20),
            text=result_string,
            justify="center",
            fill="black",
        )

    def generate_result_string(self, player_choice, computer_choice, result):
        beats_relation = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

        if result == "player":
            verb = "beats"
            result_string = f"{player_choice.capitalize()} {verb} {computer_choice.capitalize()}\nPlayer Wins!"
        elif result == "computer":
            verb = "beaten by"
            result_string = f"{player_choice.capitalize()} {verb} {computer_choice.capitalize()}\nComputer Wins!"
        else:
            result_string = f"It's a draw!\nBoth chose {player_choice.capitalize()}"

        return result_string

    def update_score_canvas(self):
        player_score, computer_score = self.game.get_scores()
        self.score_canvas.itemconfig(self.player_score_text, text=str(player_score))
        self.score_canvas.itemconfig(self.computer_score_text, text=str(computer_score))

        if player_score == 5:
            self.game_over("Player")
        elif computer_score == 5:
            self.game_over("Computer")

    def game_over(self, winner):
        self.game_canvas.delete("all")

        self.game_canvas.create_text(
            224, 186, font=("TkFixedFont", 36), text=f"{winner} Wins!", fill="white"
        )

        replay_button = Button(
            self.game_canvas,
            text="Replay",
            command=self.reset_game,
            font=("TkFixedFont", 18),
        )
        self.game_canvas.create_window(224, 262, window=replay_button)

    def reset_game(self):
        self.game.reset()

        self.game_canvas.delete("all")
        self.game_canvas.create_image(224, 152, image=self.game_img, anchor=CENTER)
        self.game_canvas.create_text(
            224,
            352,
            font=("TkFixedFont", 28),
            text="Click a\nButton Below!",
            fill="white",
            justify="center",
        )

        self.score_canvas.itemconfig(self.player_score_text, text="0")
        self.score_canvas.itemconfig(self.computer_score_text, text="0")
