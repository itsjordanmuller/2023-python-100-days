import tkinter as tk
from tkinter import ttk, filedialog


def on_closing():
    root.destroy()


def select_all(event):
    folder_path_entry.selection_range(0, tk.END)
    return "break"


def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_selected)


root = tk.Tk()
root.title("File Types in Folder")

frame1 = ttk.Frame(root)
frame1.pack(padx=20, pady=5, fill="x", expand=True)

folder_path_label = ttk.Label(frame1, text="Enter folder path:")
folder_path_label.grid(column=0, row=0, sticky=tk.W, columnspan=3)

folder_path_entry = ttk.Entry(frame1, width=40)
folder_path_entry.grid(column=0, row=1, sticky=(tk.W, tk.E), columnspan=3)
folder_path_entry.bind("<Control-a>", select_all)

browse_button = ttk.Button(frame1, text="Browse", command=browse_folder)
browse_button.grid(column=1, row=0)
scan_button = ttk.Button(frame1, text="Analyze", command=lambda: None)
scan_button.grid(column=2, row=0, sticky=tk.W)

root.mainloop()
