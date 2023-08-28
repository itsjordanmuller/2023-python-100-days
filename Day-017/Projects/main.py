from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# question_1 = Question(question_data[0]["text"], question_data[0]["answer"])
# print(question_1.text, question_1.answer)

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)

quiz = QuizBrain(question_bank)
quiz.next_question()
