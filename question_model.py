# question_model.py

import random

class Question:
    question_count = 0

    def __init__(self, question_text, question_answer):
        Question.question_count += 1
        self.code = f"Q{Question.question_count:03}"
        self.text = f"{question_text} (True/False)"
        self.answer = question_answer

    def __str__(self):
        return f"{self.code}: {self.text} (Answer: {self.answer})"


class QuestionSelector:
    @staticmethod
    def get_random_questions(question_list, number_of_questions):
        if number_of_questions > len(question_list):
            number_of_questions = len(question_list)
        return random.sample(question_list, number_of_questions)