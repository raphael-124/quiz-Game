# main.py

from question_model import Question, QuestionSelector
from data import quiz_data

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{current_question.code}: {current_question.text}\nYour answer: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().lower() == correct_answer.lower():
            self.score += 1
            print("✅ You got it right!")
        else:
            print("❌ That’s wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")


# 1️⃣ Convert data into Question objects
question_bank = [Question(q["question"], q["answer"]) for q in quiz_data]

# 2️⃣ Randomly pick, say, 10 questions
random_questions = QuestionSelector.get_random_questions(question_bank, 10)

# 3️⃣ Start the quiz
quiz = QuizBrain(random_questions)

while quiz.still_has_questions():
    quiz.next_question()

print("🎉 You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}.")