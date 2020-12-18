from turtle import Turtle

MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
POSITIONS = [(0, 0), (-20, 0), (20, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("purple")

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_seg = Turtle("circle")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # def collide(self):
    #     if self.head.xcor() > 270 or self.head.xcor() < -270:
    #         x = -(self.head.xcor())
    #         self.head.goto(x, self.head.ycor())
    #     if self.head.ycor() > 270 or self.head.ycor() < -270:
    #         y = -self.head.ycor()
    #         self.head.goto(self.head.xcor(), y)
