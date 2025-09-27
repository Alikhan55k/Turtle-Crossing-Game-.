FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,expression):
        super().__init__()
        expression_show = expression
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(0, 0)
        self.write(f"{expression_show}", align="center", font=FONT)



