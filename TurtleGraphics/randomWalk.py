from turtle import Turtle, Screen
import random

tut = Turtle()
screen = Screen()
screen.screensize(500,500)
screen.colormode(255)
tut.pensize(10)
tut.speed("fastest")

movements = [0, 90, 180, 270]


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    c = (r, g, b)
    return c


for i in range(200):
    tut.color(color())
    tut.forward(50)
    tut.setheading(random.choice(movements))

screen.exitonclick()
