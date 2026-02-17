from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width= 800, height= 600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(key="Up", fun= r_paddle.up)
screen.onkey(key="Down", fun= r_paddle.down)
screen.onkey(key="w", fun= l_paddle.up)
screen.onkey(key="s", fun= l_paddle.down)

game_on = True


while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        

    # detect if the r_paddle misses the ball
    if ball.xcor() > 380:
        score.scored(l_paddle="scored")
        ball.reset_position()

    # detect if the l_paddle misses the ball
    if ball.xcor() < -380:
        score.scored(r_paddle="scored")
        ball.reset_position()

        
        
screen.exitonclick()