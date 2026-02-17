import turtle as t
import random

t.colormode(255)
jim = t
n = 30

for _ in range(100):
    tup = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    jim.color(tup)
    jim.speed(0)
    jim.circle(100)
    jim.left(n + 1)
