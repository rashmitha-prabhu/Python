import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:

    scoreboard.up_level()
    time.sleep(0.1)
    screen.update()
    car.new_car()
    car.move()

    if car.collision(player):
        scoreboard.collision()
        game_is_on = False

    if player.win():
        car.up_level()
        scoreboard.level_up()
        player.restart()

screen.exitonclick()
