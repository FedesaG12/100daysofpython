from turtle import Turtle, Screen
from random import random


def draw_shape(n):
    jim = Turtle()
    while n >= 3:
        tup = (random(), random(), random())
        jim.pencolor(tup)
        for i in range(n):
            jim.fd(30)
            jim.right(360 / n)
            jim.fd(30)
        n -= 1
    screen = Screen()
    screen.exitonclick()


draw_shape(11)
