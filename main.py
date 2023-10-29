from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import BlockManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("Breakout")
screen.tracer(0)
STARTING_POSITION = (0, -250)

paddle = Paddle(STARTING_POSITION)
ball = Ball()
scoreboard = Scoreboard()
block_manager = BlockManager()
block_manager.place_blocks(scoreboard.level)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    paddle.update(screen)
    ball.update(paddle=paddle)
    ball.move()

    for block in block_manager.blocks:
        if ball.distance(x=block) < 40:
            ball.collide_with_block(block)
            block_manager.blocks.remove(block)
            block.ht()
            if block.color()[0] == "blue":
                scoreboard.update_score(1)
            elif block.color()[0] == "green" or block.color()[0] == "yellow":
                scoreboard.update_score(4)
            elif block.color()[0] == "orange" or block.color()[0] == "red":
                scoreboard.update_score(7)
                ball.speed_increase += 1
                if ball.speed_increase == 1:
                    ball.increase_speed()

    if ball.ycor() < -280:
        ball.reset_position(scoreboard.level)
        scoreboard.lives -= 1
        paddle.collisions = 0
        scoreboard.update_scoreboard()

    if not block_manager.blocks:
        scoreboard.level += 1
        block_manager.place_blocks(scoreboard.level)
        ball.reset_position(scoreboard.level)
        paddle.collisions = 0
        scoreboard.lives += 1

    if scoreboard.lives == 0:
        game_is_on = False
        screen.clear()
        screen.bgcolor("black")
        scoreboard.game_over()

screen.exitonclick()
