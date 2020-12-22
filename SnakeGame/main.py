from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


def set_screen():
    screen.clear()
    screen.setup(600, 600)
    screen.tracer(0)
    screen.bgcolor("black")
    screen.title("Snake Game")


screen = Screen()
scoreboard = ScoreBoard()


def restart():
    set_screen()
    snake = Snake()
    food = Food()
    scoreboard.update_board()
    scoreboard.new_high_score()
    is_on = True

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.update()

    while is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 20:
            food.refresh()
            snake.extend()
            scoreboard.update_score()

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            is_on = False
            scoreboard.retry()
            screen.listen()
            screen.onkey(restart, "space")
            snake.snake_reset()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                is_on = False
                scoreboard.retry()
                screen.listen()
                screen.onkey(restart, "space")
                snake.snake_reset()

    screen.exitonclick()


restart()
