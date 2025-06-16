import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
direction = [0, 90, 180, 270]
t.colormode(255)
tim.speed("fastest")
tim.pensize(10)


def randomize():
    tim.pencolor(random_col())
    tim.setheading(random.choice(direction))
    tim.forward(30)

def random_col():
    r =random.randint(0, 255)
    g = random.randint(0, 255)
    b =random.randint(0, 255)
    return (r, g, b)

for _ in range(250):
    randomize()

screen = t.Screen()
screen.exitonclick()
