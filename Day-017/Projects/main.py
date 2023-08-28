from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# question_1 = Question(question_data[0]["text"], question_data[0]["answer"])
# print(question_1.text, question_1.answer)

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)

quiz = QuizBrain(question_bank)
# quiz.next_question()
# quiz.still_has_questions()

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the entire quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
