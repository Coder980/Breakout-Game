from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.lives = 5
        self.level = 1
        self.get_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(300, 280)
        self.write(f"Lives: {self.lives} | High Score: {self.high_score} | Score: {self.score}", align="center", font=("Courier", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 50, "normal"))
        with open("high_score.csv", "a+") as file:
            if self.score > self.high_score:
                self.goto(0, 50)
                self.write(f"New High Score!", align="center", font=("Courier", 50, "normal"))
                file.write(f"{self.score}\n")
            else:
                self.goto(-50, 50)
                self.write(f"High Score: {self.high_score}", align="center", font=("Courier", 50, "normal"))

    def update_score(self, score):
        self.score += score
        self.update_scoreboard()

    def get_high_score(self):
        with open("high_score.csv", "a+") as file:
            file.seek(0)
            high_scores = [line.strip() for line in file.readlines()]

            for score in high_scores:
                if int(score) > self.high_score:
                    self.high_score = int(score)
