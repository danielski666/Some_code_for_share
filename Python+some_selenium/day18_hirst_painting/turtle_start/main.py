import turtle
from turtle import Turtle, Screen

turtle_timmy = Turtle()
turtle_timmy.shape("turtle")
colors = ["green", "yellow", "red", "blue", "purple", "pink", "brown"]



def move(steps):
    for _ in range(steps):
        angle = 360 / steps
        turtle_timmy.right(angle)
        turtle_timmy.forward(100)


i, list_len = 3, len(colors)
for color in colors:
    if list_len <= 7:
        turtle_timmy.color(color)
        move(i)
        i+=1

screen = Screen()
screen.exitonclick()
