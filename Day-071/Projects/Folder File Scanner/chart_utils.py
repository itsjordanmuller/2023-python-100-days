from collections import Counter
import matplotlib.pyplot as plt


def update_chart(folder_path, ax, canvas, scan_folder):
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
