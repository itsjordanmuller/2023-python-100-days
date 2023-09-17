from tkinter import *


class UserInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")

        self.canvas_size = 128
        self.canvases = []

        self.canvas_states = {}

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

                self.canvas_states[canvas] = "Empty"

        self.window.mainloop()

    def place_x(self, event):
        canvas = event.widget

        if self.canvas_states[canvas] == "Empty":
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()

            canvas.create_image(canvas_width // 2, canvas_height // 2, image=self.x_img)

            canvas.configure(bg="red")

            self.canvas_states[canvas] = "X"

    def place_o(self, event):
        canvas = event.widget

        if self.canvas_states[canvas] == "Empty":
            canvas_width = canvas.winfo_width()
            canvas_height = canvas.winfo_height()

            canvas.create_image(canvas_width // 2, canvas_height // 2, image=self.o_img)

            canvas.configure(bg="blue")

            self.canvas_states[canvas] = "O"
