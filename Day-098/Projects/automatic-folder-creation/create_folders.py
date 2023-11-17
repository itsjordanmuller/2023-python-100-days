import os
import csv

csv_file = "folders.csv"


def create_folders_with_readmes():
    """Create folders with README.md files."""
    with open(csv_file, newline="") as data:
        reader = csv.DictReader(data)
        for row in reader:
            folder_name = row["Folder Name"]
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
                print(f"Created folder: {folder_name}")
            # create_readme(folder_name)


def create_folders_without_readmes():
    """Create folders without README.md files."""
    with open(csv_file, newline="") as data:
        reader = csv.DictReader(data)
        for row in reader:
            folder_name = row["Folder Name"]
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
                print(f"Created folder: {folder_name}")


if os.path.exists(csv_file):
    print(f"Found '{csv_file}' file.")
else:
    print(f"No '{csv_file}' file found in the current directory.")
