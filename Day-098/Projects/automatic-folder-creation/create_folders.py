import os
import csv

csv_file = "folders.csv"

if os.path.exists(csv_file):
    print(f"Found '{csv_file}' file.")
else:
    print(f"No '{csv_file}' file found in the current directory.")
