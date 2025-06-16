from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_length = []
        self.create_snake()
        self.head = self.snake_length[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_length.append(snake)

    def move(self):
        for seg_num in range(len(self.snake_length) - 1, 0, -1):
            new_x = self.snake_length[seg_num - 1].xcor()
            new_y = self.snake_length[seg_num - 1].ycor()
            self.snake_length[seg_num].setpos(new_x, new_y)
        self.snake_length[0].forward(20)

    def up(self):
        if not self.snake_length[0].heading() == DOWN:
            self.snake_length[0].setheading(UP)

    def down(self):
        if not self.snake_length[0].heading() == UP:
            self.snake_length[0].setheading(DOWN)

    def left(self):
        if not self.snake_length[0].heading() == RIGHT:
            self.snake_length[0].setheading(LEFT)

    def right(self):
        if not self.snake_length[0].heading() == LEFT:
            self.snake_length[0].setheading(RIGHT)

    def extend(self):
        self.add_segment(self.snake_length[-1].position())

    def reset_snake(self):
        for seg in self.snake_length:
            seg.goto(1000, 1000)
        self.snake_length.clear()
        self.create_snake()
        self.head = self.snake_length[0]