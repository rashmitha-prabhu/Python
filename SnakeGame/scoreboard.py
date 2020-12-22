from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score = {self.score} | High Score = {self.high_score}", False, "center", ("Courier", 12, "normal"))

    def new_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as high_score:
                high_score.write(str(self.high_score))
        self.score = 0
        self.update_board()

    def update_score(self):
        self.score += 1
        self.update_board()

    def retry(self):
        self.goto(0, 20)
        self.write("GAME OVER", False, "center", ("Courier", 15, "normal"))
        self.goto(0, -20)
        self.write("Press SPACE to RESTART", False, "center", ("Courier", 15, "normal"))
