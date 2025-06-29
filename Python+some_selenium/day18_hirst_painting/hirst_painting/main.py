###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
import turtle as t
import random

paint_size, distance = 10, 50
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.goto((-250, -250))


for _ in range(paint_size):
    home = tim.pos()
    for i in range(paint_size):
        tim.dot(20, random.choice(color_list))
        tim.forward(distance)
        if i == paint_size - 1:
            tim.setpos(home[0], home[1] + distance)
tim.hideturtle()

screen = t.Screen()
screen.exitonclick()


