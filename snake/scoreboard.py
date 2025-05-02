from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "bold"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "bold"))

    def game_over(self):
        self.clear()
        self.write(f"Game Over , your score is {self.score} ", align="center", font=("Arial", 12, "bold"))

