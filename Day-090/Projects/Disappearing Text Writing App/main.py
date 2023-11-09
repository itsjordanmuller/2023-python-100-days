import tkinter as tk


class TypingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Disappearing Text App")

        self.countdown_label = tk.Label(master, text="")
        self.countdown_label.pack()

        self.display_label = tk.Label(master, text="")
        self.display_label.pack(pady=20)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=20)
        self.entry.focus_set()
        self.entry.bind("<KeyRelease>", self.update_text)

        self.after_id = None
        self.countdown_after_ids = []

    def update_text(self, event):
        self.display_label.config(text=self.entry.get())
        self.reset_countdown()

    def reset_countdown(self):
        if self.after_id:
            self.master.after_cancel(self.after_id)
        for after_id in self.countdown_after_ids:
            self.master.after_cancel(after_id)
        self.countdown_after_ids.clear()
        self.after_id = self.master.after(1000, self.start_countdown)
        self.countdown_label.config(text="")

    def start_countdown(self):
        self.countdown_after_ids.clear()
        for i in range(3, 0, -1):
            after_id = self.master.after(1000 * (3 - i), self.update_countdown, i)
            self.countdown_after_ids.append(after_id)
        self.countdown_after_ids.append(self.master.after(3000, self.clear_text))

    def update_countdown(self, i):
        self.countdown_label.config(text=f"{i}s...")

    def clear_text(self):
        self.entry.delete(0, tk.END)
        self.display_label.config(text="")
        self.countdown_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()
