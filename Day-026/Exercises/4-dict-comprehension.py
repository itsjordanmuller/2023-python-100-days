import random


# Function to generate a random score between 1 and 100
def RandomScore():
    score = random.randint(1, 100)
    return score


print("\nDictionary Comprehension Exercise\n")

# List of student names
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Generate random scores for each student
student_scores = {name: RandomScore() for name in names}
print(f"Student Scores: {student_scores}")

# Filter students with scores of 60 or above
passed_scores = {
    student: score for (student, score) in student_scores.items() if score >= 60
}
print(f"\nPassed Scores {passed_scores}")
