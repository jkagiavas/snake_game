from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.pu()
        self.ht()
        self.goto(0, 270)
        self.score_update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_update()