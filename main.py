from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

### SCREEN / GUI ####
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)                                    # TURNS OFF ANIMATION AND NEEDS TO BE UPDATED | LINE 25
### PADDLE AND BALL ###
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
### SCOREBOARD ###
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)                                  # Pause before refresh to slow down ball
    ball.move()
    screen.update()                                              # Manually refresh screen

    # DETECT COLLISION WITH FLOOR AND CEILING
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with Right paddle
    # ball.distance(l/r.paddle) - Calls bounce if it's close to the center of the paddle
    # ball.xcor() > 320         - Calls bounce if ball is within scoring range it registers the whole body of the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 \
            or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score_a_point()
    # detect when L paddle miss
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_score_a_point()
screen.exitonclick()