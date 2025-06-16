import time
from turtle import Screen
from ball import Ball
from pads import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)


r_pad = Paddle((350, 0))
l_pad = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.onkeypress(r_pad.go_up, "Up")
screen.onkeypress(r_pad.go_down, "Down")

screen.onkeypress(l_pad.go_up, "w")
screen.onkeypress(l_pad.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect the bot and top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with paddles:
    if (ball.distance(l_pad) < 50 and ball.xcor() < -320) or \
            (ball.distance(r_pad) < 50 and ball.xcor() > 320):
        ball.pad_bounce()

    # Detect r_paddle misses:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect l_paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Check score



screen.exitonclick()
