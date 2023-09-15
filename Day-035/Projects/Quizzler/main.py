from data import get_question_data, get_categories
from question_model import Question
from quiz_brain import QuizBrain
from ui import DifficultySelector, CategorySelector, QuizInterface

selector = DifficultySelector()
difficulty = selector.get_difficulty()

category_data = get_categories()
category_selector = CategorySelector(category_data)
selected_category_id = category_selector.get_category_id()

question_data = get_question_data(difficulty, selected_category_id)

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
