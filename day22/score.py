from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0,270)  
        self.l_paddle = 0
        self.r_paddle = 0
    
    def scored(self,l_paddle = None,r_paddle = None):
        if l_paddle != None:
            self.l_paddle += 1
            self.clear()
            self.write(f"{self.l_paddle} : {self.r_paddle}", align = "center", font= ("Arial", 24, "normal"))
        elif r_paddle != None:
            self.r_paddle += 1
            self.clear()
            self.write(f"{self.l_paddle} : {self.r_paddle}", align = "center", font= ("Arial", 24, "normal"))
        else:
            pass
        