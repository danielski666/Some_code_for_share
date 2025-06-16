from turtle import Screen


class GameScreen:
    def __init__(self, l_pad, r_pad):
        self.screen = Screen()
        self.create_screen()
        self.screen.onkeypress(r_pad.go_up, "Up")
        self.screen.onkeypress(r_pad.go_down, "Down")

        self.screen.onkeypress(l_pad.go_up, "w")
        self.screen.onkeypress(l_pad.go_down, "s")

    def create_screen(self):
        self.screen = Screen()
        self.screen.setup(800, 600)
        self.screen.bgcolor("black")
        self.screen.title("Pong Game")
        self.screen.listen()
        self.screen.tracer(0)
        self.screen.exitonclick()

    def update(self):
        self.screen.update()


