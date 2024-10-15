from p5 import *
import random

WIDTH = 640
HEIGHT = 240

class Walker:
    def __init__(self, width, height):
        self.x = width / 2
        self.y = height / 2

    def show(self):
        stroke(0)
        point(self.x, self.y)

    def step(self):
        xstep = random.randint(-1, 2)
        ystep = random.randint(-1, 2)

        self.x += xstep
        self.y += ystep

walker = Walker(WIDTH, HEIGHT)

def setup():
    size (WIDTH, HEIGHT)
    background(255)

def draw():
    walker.step()
    walker.show()


if __name__ == "__main__":
    run()
