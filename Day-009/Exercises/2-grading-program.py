student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"
    else:
        print("Input Error")

print(student_grades)
