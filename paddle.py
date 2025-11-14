from turtle import Turtle

class Paddle(Turtle):
    """Vertical paddle that can move up and down."""

    def __init__(self, x_position, speed=20):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_position, 0)
        self.speed_step = speed

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + self.speed_step)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - self.speed_step)

