import random


class TextManager:
    def __init__(self, canvas, font=("Courier", 24)):
        self.canvas = canvas
        self.font = font
        self.shuffled_text = self.shuffle_alphabets()
        self.letter_ids = []

    def shuffle_alphabets(self):
        alphabets = list("abcdefghijklmnopqrstuvwxyz")
        random.shuffle(alphabets)
        return "".join(alphabets)

    def display_shuffled_text(self):
        x_offset = 272 - (len(self.shuffled_text) * 7)
        for index, letter in enumerate(self.shuffled_text):
            letter_id = self.canvas.create_text(
                x_offset + (index * 25),
                100,
                text=letter,
                font=self.font,
                fill="gray",
                tags="shuffled_letter",
            )
            self.letter_ids.append(letter_id)

    def update_displayed_text_color(self, typed_text):
        for index, letter_id in enumerate(self.letter_ids):
            if index < len(typed_text):
                letter_color = (
                    "green" if self.shuffled_text[index] == typed_text[index] else "red"
                )
                self.canvas.itemconfig(letter_id, fill=letter_color)
            else:
                self.canvas.itemconfig(letter_id, fill="gray")
