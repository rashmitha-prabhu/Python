from turtle import Turtle

rPad = (350, 0)
lPad = (-350, 0)


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)

    def go_up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(), self.ycor()+20)

    def go_down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor() - 20)

    def reset_right(self):
        self.goto(rPad)

    def reset_left(self):
        self.goto(lPad)

