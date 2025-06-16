from turtle import Turtle

from screen import GameScreen


class Paddle(Turtle, GameScreen):
    def __init__(self, start_pos, multi=False):
        super().__init__()
        self.shape("square")
        self.multi = multi
        self.start_pos = start_pos
        self.create_pad()

    def create_pad(self):
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.setpos(self.start_pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)