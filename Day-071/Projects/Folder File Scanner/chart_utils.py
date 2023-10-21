from collections import Counter
import matplotlib.pyplot as plt


from collections import Counter
import matplotlib.pyplot as plt


def update_chart(folder_path, ax, canvas, scan_folder):
    file_types, lines_count = scan_folder(folder_path)
    type_lines_counter = Counter()

    for file_type, lines in zip(file_types, lines_count):
        type_lines_counter[file_type] += lines

    labels = list(type_lines_counter.keys())
    sizes = list(type_lines_counter.values())

    colors = [
        "#F06529"
        if label == ".html"
        else "#2965f1"
        if label == ".css"
        else "#f7df1e"
        if label == ".js"
        else None
        for label in labels
    ]

    ax.clear()
    ax.axis("off")

    patches, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct=lambda p: f"{p:.1f}%\n({int(p*sum(sizes)/100)} lines)",
        startangle=90,
        colors=colors,
    )

    color_cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]

    color_iter = iter(color_cycle)
    for color, patch in zip(colors, patches):
        if color is None:
            patch.set_facecolor(next(color_iter))

    ax.axis("equal")
    canvas.draw()
