from turtle import Turtle, Screen
import random

tut = Turtle()
screen = Screen()
screen.colormode(255)
# tut.pensize(3)
tut.speed("fastest")


def set_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    c = (r, g, b)
    return c


for i in range(72):
    tut.color(set_color())
    tut.circle(100)
    tut.right(5)

screen.exitonclick()
