from turtle import Turtle 
class Scoreboard(Turtle):
    
    def __init__(self):
        self.score = 0
        super().__init__()
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.record()

    def record(self):
        self.clear()
        self.write(f"score : {self.score} ", False , align = "center", font=("Arial",10,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over ", False , align = "center", font=("Arial",24,"normal"))

    def increase(self):
        self.score += 1

        
   