from question_model import Question
from data import question_data

question_1 = Question(question_data[0]["text"], question_data[0]["answer"])
print(question_1.text, question_1.answer)
