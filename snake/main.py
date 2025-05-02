from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
food =Food()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY Snake Game")
screen.tracer(0)

snake=Snake()
score=Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()