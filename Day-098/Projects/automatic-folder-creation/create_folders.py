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
            create_readme(folder_name)


def create_folders_without_readmes():
    """Create folders without README.md files."""
    with open(csv_file, newline="") as data:
        reader = csv.DictReader(data)
        for row in reader:
            folder_name = row["Folder Name"]
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
                print(f"Created folder: {folder_name}")


def create_only_readmes():
    """Create README.md files in existing folders."""
    with open(csv_file, newline="") as data:
        reader = csv.DictReader(data)
        for row in reader:
            folder_name = row["Folder Name"]
            if os.path.exists(folder_name) and os.path.isdir(folder_name):
                create_readme(folder_name)
            else:
                print(f"Folder does not exist: {folder_name}")


def create_readme(folder_name):
    """Create a README.md file in the specified folder."""
    readme_path = os.path.join(folder_name, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as readme_file:
            readme_file.write(f"# {folder_name}\n")
            print(f"Created README.md in {folder_name}")
    else:
        print(f"README.md already exists in {folder_name}")


def rename_folders():
    """Rename folders based on CSV data."""
    with open(csv_file, newline="") as data:
        reader = csv.DictReader(data)
        for row in reader:
            original_name = row["Folder Name"]
            new_name = row["New Name"]

            if os.path.exists(original_name) and os.path.isdir(original_name):
                os.rename(original_name, new_name)
                print(f"Renamed folder {original_name} to {new_name}")
            else:
                print(f"Folder does not exist: {original_name}")


def rename_folders_and_update_readmes():
    """Rename folders and update README.md files."""
    with open(csv_file, newline="") as data:
        reader = csv.DictReader(data)
        for row in reader:
            original_name = row["Folder Name"]
            new_name = row["New Name"]

            if os.path.exists(original_name) and os.path.isdir(original_name):
                os.rename(original_name, new_name)
                print(f"Renamed folder {original_name} to {new_name}")

                readme_path = os.path.join(new_name, "README.md")
                if os.path.exists(readme_path):
                    with open(readme_path, "r") as file:
                        lines = file.readlines()
                    with open(readme_path, "w") as file:
                        lines[0] = f"# {new_name}\n"
                        file.writelines(lines)
                        print(f"Updated README.md in {new_name}")
            else:
                print(f"Folder does not exist: {original_name}")


if os.path.exists(csv_file):
    print("\nSelect an option:")
    print("1: Create folders with README.md files.")
    print("2: Create folders without README.md files.")
    print("3: Create README.md files in existing folders.")
    choice = input("\nEnter your choice (1, 2, or 3): ")

    if choice == "1":
        create_folders_with_readmes()
    elif choice == "2":
        create_folders_without_readmes()
    elif choice == "3":
        create_only_readmes()
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
else:
    print(f"No '{csv_file}' file found in the current directory.")
