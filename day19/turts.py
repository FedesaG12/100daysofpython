from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle would win the race? Enter a color: "
)  # the dialoge will appear on the window and ask the user to enter something.
screen.setup(width=500, height=400)  # This is needed to set the screen size
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
dic = {}

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=(-100 + (i * 50)))
    dic[new_turtle.ycor()] = colors[i]
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

count = 0

while is_race_on:

    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)
        if turtle.xcor() >= 240:
            if user_bet == dic[turtle.ycor()]:
                print(f"you win!{user_bet} wins.")
                is_race_on = False
            else:
                print(f"you loose!{dic[turtle.ycor()]} wins.")
                is_race_on = False

screen.exitonclick()
