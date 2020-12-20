from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

# Turtle to draw dotted line in center
border = Turtle()
border.hideturtle()
border.color("white")
border.penup()
border.goto(0, 290)
border.right(90)
while border.ycor() > -300:
    border.pendown()
    border.forward(25)
    border.penup()
    border.forward(25)

rPad = Paddle((350, 0))
lPad = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(rPad.go_up, "Up")
screen.onkey(rPad.go_down, "Down")
screen.onkey(lPad.go_up, "w")
screen.onkey(lPad.go_down, "s")

is_on = True
while is_on:
    time.sleep(ball.move_speed)
    scoreboard.update_score()
    screen.update()
    ball.move()

    # Ball hits paddle
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
        ball.move_speed *= 0.9

    # Ball goes out of screen
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_score += 1
        rPad.reset_right()
        lPad.reset_left()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_score += 1
        rPad.reset_right()
        lPad.reset_left()

    # Collision with paddle
    if ball.xcor() > 330 and ball.distance(rPad) < 50 or ball.xcor() < -330 and ball.distance(lPad) < 50:
        ball.collide()

screen.exitonclick()
