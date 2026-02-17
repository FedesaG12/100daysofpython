from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.lst_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random .randint(1,6)
        if random_chance == 1:
            cars = Turtle()
            cars.penup()
            cars.shape("square")
            cars.color(random.choice(COLORS))
            cars.shapesize(stretch_len= 2, stretch_wid= 1)
            cars.goto(300, random.randint(-250,250))
            self.lst_cars.append(cars)

    def move_cars(self):
       for car in self.lst_cars:
           car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT