from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_cor=10
        self.y_cor=10
        self.ball_speed=0.1

    def bounce_x(self):
        self.x_cor=self.x_cor*-1
    def bounce_y(self):
        self.y_cor=self.y_cor*-1
    def move(self):
        new_y=self.ycor()+self.y_cor
        new_x=self.xcor()+self.x_cor
        self.goto(new_x,new_y)
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
    def increase_speed(self):
        self.ball_speed=self.ball_speed*0.9
    def speed_reset(self):
        self.ball_speed=0.1



