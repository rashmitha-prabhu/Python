from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def new_car(self):
        create_car = random.randint(1, 10)
        if create_car == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.goto(280, random.randint(-6, 6) * 40)
            car.color(random.choice(COLORS))
            car.setheading(180)
            car.shapesize(1, 2)
            self.all_cars.append(car)

    def collision(self, player):
        for car in self.all_cars:
            if car.distance(player) < 30:
                return True

    def up_level(self):
        self.car_speed += MOVE_INCREMENT
