class QuizBrain:
    """Manages quiz logic and tracking of user's progress and score.

    Attributes:
        question_number (int): Tracks the number of questions asked.
        question_list (list): List of all questions in the quiz.
        score (int): The user's current score.
    """

    def __init__(self, question_list):
        """Initializes QuizBrain with a list of questions."""
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """Displays the next question and prompts the user for an answer."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): "
        )
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """Returns True if there are more questions to ask; otherwise False."""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """Checks the user's answer against the correct answer and updates the score."""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
