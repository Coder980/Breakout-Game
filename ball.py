from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.85)
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
        self.goto(0, -220)
        self.speed_increase = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def increase_speed(self):
        self.move_speed = round(self.move_speed/2, 3)

    def reset_position(self, level):
        self.goto(0, -220)
        if level == 1:
            self.move_speed = 0.05
        elif level == 2:
            self.move_speed = 0.04
        elif level == 3:
            self.move_speed = 0.03
        elif level == 4:
            self.move_speed = 0.03
        elif level == 5:
            self.move_speed = 0.02
        elif level == 6:
            self.move_speed = 0.02
        elif level == 7:
            self.move_speed = 0.01
        elif level == 8:
            self.move_speed = 0.01
        else:
            self.move_speed = round(0.01/2, 3)
        self.y_move = -10
        self.bounce_y()
        self.speed_increase = 0

    def level1(self):
        pass

    def update(self, paddle=None):
        if self.xcor() > 470 or self.xcor() < -480:
            self.bounce_x()

        if self.xcor() > 480:
            self.goto(460, self.ycor())
        elif self.xcor() < -490:
            self.goto(-460, self.ycor())

        if self.ycor() > 280:
            self.bounce_y()

        if self.collide_with_paddle(paddle):
            paddle.collisions += 1
            if paddle.collisions >= 6:
                self.speed_increase += 1
                if self.speed_increase == 1:
                    self.increase_speed()
                self.move_speed = round(self.move_speed - 0.00001, 5)
            relative_position = self.xcor() - paddle.xcor()
            if relative_position < 0:
                self.x_move = -10
            elif relative_position > 0:
                self.x_move = 10
            else:
                self.bounce_x()
            self.bounce_y()

            if self.xcor() >= 450 and self.ycor() == -230:
                self.goto(300, -220)
            elif self.xcor() <= -450 and self.ycor() == -230:
                self.goto(-300, -220)

    def collide_with_paddle(self, paddle):
        if self.distance(x=paddle) < 140 and -220 > self.ycor() >= -250:
            return True

    def collide_with_block(self, block):
        if (self.xcor() <= block.xcor() - 30 or self.xcor() >= block.xcor() + 30) and (
                self.ycor() >= block.ycor() + 20 or self.ycor() <= block.ycor() - 20):
            # All Edges
            self.bounce_x()
            self.bounce_y()
        elif self.xcor() <= block.xcor() - 30 or self.xcor() >= block.xcor() + 30:
            # Left and Right Walls
            self.bounce_x()
        else:
            # Top and Bottom
            self.bounce_y()
