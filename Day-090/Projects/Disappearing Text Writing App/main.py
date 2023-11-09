import tkinter as tk


class TypingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Disappearing Text App")

        self.master.geometry("800x600")

        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=2)
        master.grid_columnconfigure(0, weight=1)

        top_frame = tk.Frame(master)
        top_frame.grid(row=0, column=0, sticky="nsew")

        bottom_frame = tk.Frame(master)
        bottom_frame.grid(row=1, column=0, sticky="nsew")

        self.countdown_label = tk.Label(top_frame, text="", wraplength=400)
        self.countdown_label.pack()

        self.display_label = tk.Label(top_frame, text="", fg="black", wraplength=400)
        self.display_label.pack(pady=20)

        self.text = tk.Text(bottom_frame, wrap="char", height=10)
        self.text.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH, pady=20)
        self.text.bind("<KeyRelease>", self.update_text)
        self.text.focus_set()

        self.after_id = None
        self.countdown_after_ids = []

        self.fade_colors = {
            3: "#555555",
            2: "#888888",
            1: "#bbbbbb",
        }

    def update_text(self, event):
        text_content = self.text.get("1.0", "end-1c")
        self.display_label.config(text=text_content)
        self.reset_countdown()

    def reset_countdown(self):
        if self.after_id:
            self.master.after_cancel(self.after_id)
        for after_id in self.countdown_after_ids:
            self.master.after_cancel(after_id)
        self.countdown_after_ids.clear()
        self.display_label.config(fg="black")
        self.after_id = self.master.after(1000, self.start_countdown)
        self.countdown_label.config(text="")

    def start_countdown(self):
        self.countdown_after_ids.clear()
        self.update_opacity(3)
        for i in range(3, 0, -1):
            self.countdown_after_ids.append(
                self.master.after(1000 * (3 - i), self.update_countdown, i)
            )
            self.countdown_after_ids.append(
                self.master.after(1000 * (3 - i), self.update_opacity, i)
            )
        self.countdown_after_ids.append(self.master.after(3000, self.clear_text))

    def update_countdown(self, i):
        self.countdown_label.config(text=f"{i}s...")

    def update_opacity(self, step):
        self.display_label.config(fg=self.fade_colors[step])

    def clear_text(self):
        self.text.delete("1.0", tk.END)
        self.display_label.config(text="")
        self.countdown_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingApp(root)
    root.mainloop()
