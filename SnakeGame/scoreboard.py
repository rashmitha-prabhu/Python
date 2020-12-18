from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.write(f"Score = {self.score}", False, "center", ("Courier", 12, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Courier", 15, "normal"))
