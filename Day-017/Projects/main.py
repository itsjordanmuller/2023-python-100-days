from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

print("\nTrivia Quiz Game\n")

# Initialize empty question bank
question_bank = []
# Building question bank from data
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create Quiz instance with questions
quiz = QuizBrain(question_bank)

# Running the quiz
while quiz.still_has_questions():
    quiz.next_question()

# End of quiz summary
print("You've completed the entire quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
