from turtle import Turtle

FONT = ('Verdana', 15, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.updated_scoreboard()

    def updated_scoreboard(self):
        self.goto(-100, 250)
        self.write(f'Score: {self.l_score}', align=ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(f'Score: {self.r_score}', align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.updated_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.updated_scoreboard()

    def gameover(self):
        self.write('Game Over...', align=ALIGNMENT, font=FONT)
