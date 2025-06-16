import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(1, 1)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_pos, y_pos = random.randint(-280, 280), random.randint(-280, 280)
        self.setpos(x_pos, y_pos)

