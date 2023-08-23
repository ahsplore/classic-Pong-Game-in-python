from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, color_in):
        super().__init__()
        self.position = position
        self.color_in = color_in
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color(self.color_in)
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(self.position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
