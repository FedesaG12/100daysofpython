from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()


def move_forward():
    return jim.fd(10)


def move_backward():
    return jim.back(10)


def counter_clockwise():
    return jim.left(10)


def clockwise():
    return jim.right(10)


def clear_drawing():
    jim.home()
    return jim.clear()


screen.listen()  # this one is the event listner
screen.onkey(key="w", fun=move_forward)  # this one is the higher order.
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()
