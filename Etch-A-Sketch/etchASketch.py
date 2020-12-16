from turtle import Turtle, Screen
import random

tut = Turtle()
screen = Screen()

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'black', 'orange']


def random_color():
    tut.color(random.choice(colors))


def move_front():
    tut.forward(10)


def move_back():
    tut.backward(10)


def move_right():
    tut.right(5)


def move_left():
    tut.left(5)


def clear_screen():
    tut.home()
    tut.clear()


def increase():
    tut.pensize(tut.pensize()+5)


def decrease():
    tut.pensize(tut.pensize()-5)


screen.listen()
screen.onkey(move_front, "Up")
screen.onkey(move_back, "Down")
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(clear_screen, "space")
screen.onkey(random_color, "c")
screen.onkey(increase, "p")
screen.onkey(decrease, "m")

screen.exitonclick()
