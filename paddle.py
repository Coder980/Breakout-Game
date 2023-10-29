from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.collisions = 0
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=13)
        self.color("steel blue")
        self.penup()
        self.goto(self.position)

    def update(self, screen):
        self.setx(screen.getcanvas().winfo_pointerx() - screen.getcanvas().winfo_rootx()-500)
        if self.xcor() > 370:
            self.setx(359)
        elif self.xcor() < -380:
            self.setx(-370)
