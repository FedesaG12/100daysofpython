from turtle import Turtle, Screen
import random
import turtle as t

t.colormode(255)
jim = Turtle()
directions = [0, 90, 180, 270]

for _ in range(200):
    tup = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    jim.color(tup)
    jim.speed(0)
    angle = random.randint(0, 3)
    jim.pensize(5)
    jim.fd(30)
    jim.setheading(directions[angle])

screen = Screen()
screen.exitonclick()
