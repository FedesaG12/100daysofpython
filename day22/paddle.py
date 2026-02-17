from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, cor = ()):
        super().__init__()
        # self.paddle = Turtle()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(5,1)
        self.goto(cor)
        
    def up(self):
        new_y = self.ycor() + 50
        self.up = self.goto(self.xcor(), new_y)
    
    def down(self):
        new_y = self.ycor() - 50
        self.up = self.goto(self.xcor(), new_y)