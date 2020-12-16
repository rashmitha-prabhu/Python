from turtle import Turtle, Screen
import random

tut = Turtle()
screen = Screen()
screen.colormode(255)
tut.hideturtle()
tut.penup()
tut.setposition(-200, -250)
tut.pendown()
tut.speed("fastest")

c = [(61, 121, 170), (50, 96, 57), (238, 203, 71), (182, 64, 49), (179, 173, 36), (221, 172, 198), (182, 51, 56),
     (211, 87, 57), (46, 46, 95), (209, 163, 187), (133, 160, 186), (38, 39, 80), (37, 84, 45), (244, 199, 4),
     (149, 169, 152)]


for i in range(10):
    for j in range(10):
        tut.color(random.choice(c))
        tut.pendown()
        tut.dot(20)
        tut.penup()
        tut.forward(50)
    tut.penup()
    tut.setposition(tut.xcor() - 500, tut.ycor() + 50)

screen.exitonclick()
