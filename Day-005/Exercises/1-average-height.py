print("\nAverage Height Calculator\n")

# User input for student heights, comma-separated
student_heights = input("Input a list of student heights (comma-separated):\n").split(
    ","
)

# Convert each height from string to integer
for n in range(len(student_heights)):
    student_heights[n] = int(
        student_heights[n].strip()
    )  # Added strip() to remove potential whitespace

# Initialize total height and student count
total_height = 0
# Count number of students
student_count = len(student_heights)

# Sum up total height
for height in student_heights:
    total_height += height

# Calculate and display average height
average_height = round(total_height / student_count)
print(f"\nAverage Height: {average_height}")
