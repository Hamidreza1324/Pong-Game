from turtle import Turtle
import random

class Ball(Turtle):
    """Ball with movement, bouncing, speed scaling, and color change."""

    COLORS = ["white", "cyan", "yellow", "magenta", "orange", "lime"]

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1
        self.change_color()

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        self.change_color()

    def reset_position(self):
        """Center the ball and reset speed."""
        self.goto(0, 0)
        self.move_speed = 0.08
        self.bounce_x()

    def change_color(self):
        """Randomly change color on bounce."""
        self.color(random.choice(self.COLORS))

