from p5 import *
import random

WIDTH = 640
HEIGHT = 240

def accept_reject():
    while True:
        r1 = random.random()
        probability = r1
        r2 = random.random()
        if r2 < probability:
            return r1 * 2

class Walker:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2

    def show(self):
        stroke(0)
        point(self.x, self.y)

    def step(self):
        r1 = random.random()
        r2 = random.random()

        xstep = accept_reject()
        ystep = accept_reject()

        if r1 < .5:
            self.x += -1 * xstep
        else:
            self.x += xstep

        if r2 < .5:
            self.y += -1 * ystep
        else:
            self.y += ystep

walker = Walker()

def setup():
    size(WIDTH, HEIGHT)
    background(204)

def draw():
    walker.step()
    walker.show()

run()
