from turtle import Turtle 
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.record()

    def record(self):
        self.clear()
        self.write(f"score : {self.score} High score {self.high_score}", False , align = "center", font=("Arial",10,"normal"))

    def reset(self):
        if self.high_score > self.score:
            self.high_score = self.score
        self.score = 0
        self.record()
        
    def increase(self):
        self.score += 1
        self.record()