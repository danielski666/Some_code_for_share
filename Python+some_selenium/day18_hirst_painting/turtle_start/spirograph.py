import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
t.colormode(255)
tim.speed("fastest")


def randomize(step):
    tim.pencolor(random_col())
    tim.circle(100)
    tim.setheading(tim.heading() + step)


def random_col():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spiro(step):
    for _ in range(int(360 / step)):
        randomize(step)


draw_spiro(5)
screen = t.Screen()
screen.exitonclick()
