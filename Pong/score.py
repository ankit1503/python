from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score,align='center',font=('Arial',50,'bold'))
        self.goto(100, 200)
        self.write(self.r_score,align='center',font=('Arial',50,'bold'))

    def l_score_increase(self):
        self.l_score=self.l_score+1
    def r_score_increase(self):
        self.r_score=self.r_score+1

