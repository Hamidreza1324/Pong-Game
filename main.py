from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# --- Screen Setup ---
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# --- Objects ---
r_paddle = Paddle(350, speed=25)
l_paddle = Paddle(-350, speed=25)
ball = Ball()
scoreboard = Scoreboard()

# --- Controls ---
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# --- Countdown Before Start ---
for i in range(3, 0, -1):
    scoreboard.clear_message()        # Clear previous text
    scoreboard.display_message(f"Starting in {i}")
    screen.update()
    time.sleep(1)
scoreboard.clear_message()


# --- Game Loop ---
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # bounce off top/bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # paddle collision
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # right paddle miss
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # left paddle miss
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

    # --- Game Over ---
    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        winner = "Left Player" if scoreboard.l_score == 10 else "Right Player"
        scoreboard.game_over(winner)
        game_is_on = False

screen.exitonclick()
