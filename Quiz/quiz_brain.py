class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False

    def next_question(self):
        ans = input(f'Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False) :  ')
        self.check_answer(ans, self.question_list[self.question_number].answer)
        print(f"Your Current Score is : {self.score}/{self.question_number+1}")
        self.question_number += 1

    def check_answer(self, ans, c_ans):
        if ans.lower() == c_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was {c_ans}")
