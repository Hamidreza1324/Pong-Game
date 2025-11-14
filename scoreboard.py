from turtle import Turtle

class Scoreboard(Turtle):
    """Handles scoring, messages, and game-over text."""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def display_message(self, text):
        """Temporary text in center."""
        self.goto(0, 0)
        self.write(text, align="center", font=("Courier", 30, "normal"))

    def clear_message(self):
        self.clear()
        self.update_scoreboard()

    def game_over(self, winner):
        self.goto(0, -50)
        self.write(f"{winner} Wins!", align="center", font=("Courier", 36, "bold"))

