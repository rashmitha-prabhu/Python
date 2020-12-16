from turtle import Turtle, Screen
import random

tut = Turtle()
tut.shape("turtle")
screen = Screen()
tut.penup()
tut.setposition(-50, 100)
tut.pendown()
screen.colormode(255)

for i in range(3, 11):
    r = random.randint(0, 255)
    y = random.randint(0, 255)
    b = random.randint(0, 255)
    tut.pencolor(r, y, b)
    for j in range(i):
        tut.forward(100)
        deg = 360/i
        tut.right(deg)

screen.exitonclick()
