from turtle import Turtle

from ball import Ball

ALIGNMENT = "center"
FONT = ('Courier', 50, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.setpos(-100, 225)
        self.write(self.l_score, False, ALIGNMENT, FONT)
        self.setpos(100, 225)
        self.write(self.r_score, False, ALIGNMENT, FONT)


    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()