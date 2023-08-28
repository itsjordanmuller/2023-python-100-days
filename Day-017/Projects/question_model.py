class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_1 = Question("Is 2 + 2 = 5?", "False")
print(question_1.text, question_1.answer)
