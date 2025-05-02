from turtle import Screen
from ball import Ball
import time
from paddle import Paddle
from score import Score
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
score = Score()
screen.listen()

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
ball = Ball()
is_game_over = True

while is_game_over:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    #detect collision with wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.xcor() < -320 and left_paddle.distance(ball)<50 or ball.xcor() > 320 and right_paddle.distance(ball)<50:
        ball.bounce_x()
        ball.increase_speed()
    # right paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_score_increase()
        score.update_score()
        ball.speed_reset()
    #ball miss the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_score_increase()
        score.update_score()
        ball.speed_reset()

screen.exitonclick()