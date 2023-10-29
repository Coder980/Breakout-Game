from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue"]


class BlockManager:
    def __init__(self):
        self.blocks = []
        self.blocks_hit = 0

    def create_block(self, color):
        block = Turtle("square")
        block.penup()
        block.color(color)
        block.shapesize(stretch_len=3, stretch_wid=2)
        self.blocks.append(block)
        return block

    def place_blocks(self, level):
        for color in COLORS:
            x = -465
            for i in range(15):
                block = self.create_block(color)
                if color == "blue":
                    if level % 2 == 0 or level == 1:
                        block.goto(x, -40)
                    else:
                        self.blocks.remove(block)
                        block.ht()
                elif color == "green":
                    block.goto(x, 5)
                elif color == "yellow":
                    block.goto(x, 50)
                elif color == "orange":
                    block.goto(x, 95)
                else:
                    block.goto(x, 140)
                x += 66
