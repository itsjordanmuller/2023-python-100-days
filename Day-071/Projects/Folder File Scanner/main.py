import os
import tkinter as tk
from tkinter import ttk, filedialog
import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def count_lines(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        return sum(1 for line in file)


def scan_folder(folder_path):
    file_types = []
    lines_count = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[-1].lower()

            try:
                lines = count_lines(file_path)
                file_types.append(file_extension)
                lines_count.append(lines)
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")

    return file_types, lines_count


def update_chart(folder_path):
    file_types, lines_count = scan_folder(folder_path)
    type_lines_counter = Counter()

    for file_type, lines in zip(file_types, lines_count):
        type_lines_counter[file_type] += lines

    labels = list(type_lines_counter.keys())
    sizes = list(type_lines_counter.values())

    ax.clear()
    ax.axis("off")
    ax.pie(
        sizes,
        labels=labels,
        autopct=lambda p: f"{p:.1f}%\n({int(p*sum(sizes)/100)} lines)",
        startangle=90,
    )
    ax.axis("equal")

    canvas.draw()


def on_closing():
    plt.close()
    root.destroy()


def on_button_click():
    folder_path = folder_path_entry.get()
    if os.path.isdir(folder_path):
        update_chart(folder_path)
    else:
        print("Please enter a valid folder path")


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
