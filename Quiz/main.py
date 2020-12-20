from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    q = Question(item["question"], item["correct_answer"])
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    print("")

print("You've completed the quiz!!")
print(f"Your Score = {quiz.score}/{quiz.question_number}")
