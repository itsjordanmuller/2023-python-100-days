import os
import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from file_utils import count_lines, scan_folder
from chart_utils import update_chart


def on_closing():
    plt.close()
    root.destroy()


def on_button_click():
    folder_path = folder_path_entry.get()
    if os.path.isdir(folder_path):
        update_chart(folder_path, ax, canvas, scan_folder)
    else:
        print("Please enter a valid folder path")


def select_all(event):
    folder_path_entry.selection_range(0, tk.END)
    return "break"


def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_selected)


# GUI setup
root = tk.Tk()
root.title("File Types in Folder")

frame1 = ttk.Frame(root)
frame1.pack(padx=20, pady=5, fill="x", expand=True)

folder_path_label = ttk.Label(frame1, text="Enter folder path:")
folder_path_label.grid(column=0, row=0, sticky=tk.W, columnspan=3)

folder_path_entry = ttk.Entry(frame1, width=40)
folder_path_entry.grid(column=0, row=1, sticky=(tk.W, tk.E), columnspan=3)

frame1.grid_columnconfigure(0, weight=1)

folder_path_entry.bind("<Control-a>", select_all)

browse_button = ttk.Button(frame1, text="Browse", command=browse_folder)
browse_button.grid(column=1, row=0)
scan_button = ttk.Button(frame1, text="Analyze", command=on_button_click)
scan_button.grid(column=2, row=0, sticky=tk.W)

frame2 = ttk.Frame(root)
frame2.pack(padx=20, pady=15, fill=tk.BOTH, expand=True)

fig, ax = plt.subplots()
ax.axis("off")
canvas = FigureCanvasTkAgg(fig, master=frame2)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
