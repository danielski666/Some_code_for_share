from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.score = 0
        self.high_score = self.check_high_score()
        self.penup()
        self.hideturtle()
        self.setpos(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def check_high_score(self):
        h_score = 0
        with open("data.txt", "r") as data_file:
            h_score = data_file.read()
        return int(h_score)

    def update_high_score(self):
        with open("data.txt", "w") as data_file:
            data_file.write(str(self.high_score))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setpos(0, 0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)

