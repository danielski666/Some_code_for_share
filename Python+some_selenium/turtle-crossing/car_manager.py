from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.create_cars()

    def drive(self, lvl):
        for car in self.cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE - MOVE_INCREMENT * (lvl - 1)
            car.setpos(new_x, car.ycor())
            self.remove_car()

    def create_cars(self):
        for _ in range(randint(0, 4)):
            self.cars.append(self.create_car())

    @staticmethod
    def create_car():
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(1, 2)
        car.color(choice(COLORS))
        car.setpos(400, randint(-250, 250))
        return car

    def remove_car(self):
        for i in range(len(self.cars)):
            if self.cars[i].xcor() < -400:
                self.cars[i].hideturtle()
                del self.cars[i]
            elif i > 10:
                break
