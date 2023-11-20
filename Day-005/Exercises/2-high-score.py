print("\nHigh Score Finder\n")

# Get comma-separated list of student scores
student_scores = input("Input a list of student scores (comma-separated):\n").split(",")
for n in range(len(student_scores)):
    # Strip spaces and convert to int
    student_scores[n] = int(student_scores[n].strip())
print(f"\nScores: {student_scores}")

# Initialize variable for tracking the highest score
high_score = 0

# Iterate through the scores to find the highest one
for score in student_scores:
    if score > high_score:
        high_score = score

# Print the highest score found
print(f"\nThe highest score in the class is: {high_score}")
