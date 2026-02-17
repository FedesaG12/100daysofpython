import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

Count = 0

screen.listen()
screen.onkey(key= "Up",fun= player.move)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    create = car.create_car()
    car.move_cars()
    
    
    # detect the turtle collision with the car
    for create in car.lst_cars:
        if player.distance(create) <= 20:
            score.game_over()
            game_is_on = False

    #  detect if the player reache the top edge and increase the cars movement
    if player.reset():
        player.go_to_start()
        car.level_up()
        Count += 1
        score.level_count(Count)

screen.exitonclick()