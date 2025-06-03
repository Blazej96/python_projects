from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-180, 200)
        self.write("Level: ", align="center", font=FONT)
        self.goto(-90, 200)
        self.write(self.score, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)

    def level(self):
        self.score += 1
        self.update_scoreboard()

    def reset_points(self):
        self.score = 0
        self.update_scoreboard()