from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.level = 1
        self.up_level()

    def up_level(self):
        self.goto(-200, 250)
        self.clear()
        self.write(f"Level : {self.level}", False, "center", FONT)

    def collision(self):
        self.goto(0, 0)
        self.write("Game Over", False, "center", FONT)

    def level_up(self):
        self.level += 1
