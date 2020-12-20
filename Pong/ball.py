from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.angle = 45
        self.move_speed = 0.1

    def move(self):
        self.setheading(self.angle)
        self.forward(10)

    def bounce(self):
        self.angle *= -1

    def collide(self):
        self.angle = self.angle*-1 + 180

    def reset_ball(self):
        self.goto(0, 0)
        self.angle += 270
        self.move_speed = 0.1

