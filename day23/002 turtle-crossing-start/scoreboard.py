from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        
    def level_count(self, count):
        self.clear()
        self.goto(-250,250)
        self.write(f"Level: {count}", align= "left",font= FONT)
    
    def game_over(self):
        self.write("Game Over", align = "center", font = FONT)