import tkinter as tk


class TypingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Disappearing Text App")

        self.display_label = tk.Label(master, text="")
        self.display_label.pack(pady=20)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=20)
        self.entry.focus_set()
        self.entry.bind("<KeyRelease>", self.update_text)

    def update_text(self, event):
        self.display_label.config(text=self.entry.get())


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()
