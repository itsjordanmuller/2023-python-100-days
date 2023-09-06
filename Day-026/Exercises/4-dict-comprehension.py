import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]


def RandomScore():
    score = random.randint(1, 100)
    return score


student_scores = {name: RandomScore() for name in names}
print(student_scores)

passed_scores = {
    student: score for (student, score) in student_scores.items() if score >= 60
}
print(passed_scores)
