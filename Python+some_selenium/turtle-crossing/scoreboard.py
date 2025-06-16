from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.level = 0
        self.setpos(-280, 250)
        self.hideturtle()
        self.level_update()

    def level_update(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, ALIGNMENT, FONT)

    @staticmethod
    def game_over():
        g_over = Turtle()
        g_over.write("GAME OVER", False, "center", FONT)
