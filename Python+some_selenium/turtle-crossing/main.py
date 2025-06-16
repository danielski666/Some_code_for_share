import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()

game_is_on, count = True, 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if count % 6 == 0:
        car.create_cars()
    car.drive(scoreboard.level)
    screen.listen()
    screen.onkeypress(player.move, "Up")

    # check if turtle cross the road safe
    if player.ycor() > 280:
        player.go_to_start()
        scoreboard.level_update()

# check collision with cars
    for vehicle in car.cars:
        if player.distance(vehicle) < 20:
            scoreboard.game_over()
            game_is_on = False

    print(len(car.cars))

    count += 1


screen.exitonclick()