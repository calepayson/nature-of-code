from p5 import *
import random

WIDTH = 640
HEIGHT = 240

class Walker:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2

    def show(self):
        stroke(0)
        point(self.x, self.y)

    def step(self):
        r = random.random()
        if  (r < 0.01):
            xstep = random.randint(-100, 100)
            ystep = random.randint(-100, 100)
        else:
            xstep = random.randint(-1, 1)
            ystep = random.randint(-1, 1)

        self.x += xstep
        self.y += ystep

walker = Walker()

def setup():
    size(WIDTH, HEIGHT)
    background(204)

def draw():
    walker.step()
    walker.show()

run()
