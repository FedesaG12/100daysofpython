from turtle import Turtle, Screen
import random

screen = Screen()
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle would win the race? Enter a color: "
)  # the dialoge will appear on the window and ask the user to enter something.
screen.setup(width=500, height=400)  # This is needed to set the screen size


jim = Turtle()
jim.shape("turtle")
jim.color("red")
jim.penup()

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.penup()

timy = Turtle()
timy.shape("turtle")
timy.color("yellow")
timy.penup()

jimy = Turtle()
jimy.shape("turtle")
jimy.color("black")
jimy.penup()

tom = Turtle()
tom.shape("turtle")
tom.color("purple")
tom.penup()

tomy = Turtle()
tomy.shape("turtle")
tomy.color("green")
tomy.penup()


def race():
    n = -240  # this is there initial position.
    m = -240
    o = -240
    p = -240
    q = -240
    r = -240
    for _ in range(250):  # this one is used to iterrate the loop 250 times.
        tim.goto(
            x=n, y=-70
        )  # here we set the position where the turtles begin the race.
        jim.goto(x=m, y=-100)
        timy.goto(x=o, y=-40)
        jimy.goto(x=p, y=-10)
        tom.goto(x=q, y=20)
        tomy.goto(x=r, y=50)
        lst = [n, m, o, p, q, r]
        if (
            n and m and o and p and q and r > 230
        ):  # here we checked if any turtle reached the limit or the end line.
            if max(lst) == n:
                if (
                    user_bet == "blue"
                ):  # blue turtle have two chances to win or lose so we used if it wins return winner else loser.
                    return "You win! Blue is the winner"
                else:
                    return "You lose! Blue is the winner"
            elif max(lst) == m:
                if user_bet == "red":
                    return "You win! Red is the winner"
                else:
                    return "You lose! Red is the winner"
            elif max(lst) == o:
                if user_bet == "yellow":
                    return "You win! Yellow is the winner"
                else:
                    return "You lose! Yellow is the winner"
            elif max(lst) == p:
                if user_bet == "black":
                    return "You win! Black is the winner"
                else:
                    return "You lose! Black is the winner"
            elif max(lst) == q:
                if user_bet == "purple":
                    return "You win! Purple is the winner"
                else:
                    return "You lose! Purple is the winner"
            elif max(lst) == r:
                if user_bet == "green":
                    return "You win! Green is the winner"
                else:
                    return "You lose! Green is the winner"

        n += random.randint(
            3, 6
        )  # here we used random to make the turtles move randomly and win the race unpridictably.
        m += random.randint(3, 6)
        o += random.randint(3, 6)
        p += random.randint(3, 6)
        q += random.randint(3, 6)
        r += random.randint(3, 6)


print(race())

screen.exitonclick()
