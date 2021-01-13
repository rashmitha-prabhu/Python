from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.quiz_text = self.canvas.create_text(150, 125, width=280, text="Question", fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.right = PhotoImage(file="images/true.png")
        self.true = Button(text='True', image=self.right, highlightthickness=0, command=self.true_pressed)
        self.true.grid(row=2, column=0)

        self.wrong = PhotoImage(file="images/false.png")
        self.false = Button(text='False', image=self.wrong, highlightthickness=0, command=self.false_pressed)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)

        else:
            self.canvas.itemconfig(self.quiz_text, text=f"Your score : {self.quiz.score}/10")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, alert):
        if alert:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)
