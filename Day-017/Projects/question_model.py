class Question:
    """Represents a quiz question.

    Attributes:
        text (str): The question text.
        answer (str): The correct answer to the question.
    """

    def __init__(self, text, answer):
        """Initializes a new Question instance with the given text and answer."""
        self.text = text
        self.answer = answer
