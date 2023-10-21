import os
from collections import Counter


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
