import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]


def RandomScore():
    score = random.randint(1, 100)
    return score


student_scores = {name: RandomScore() for name in names}
print(student_scores)
