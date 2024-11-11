from p5 import *
import random


class Walker:
    def __init__(self):
        self.x = width / 2
        self.y = height / 2

    def step(self):
        random_number = random.random()
        xstep = 0
        ystep = 0

        if random_number < 0.5:
            xstep = random.randint(-1, 1)
            ystep = random.randint(-1, 1)
        else:
            if mouse_x > self.x:
                xstep = 1
            elif mouse_x < self.x:
                xstep = -1
            if mouse_y > self.y:
                ystep = 1
            elif mouse_y < self.y:
                ystep = -1

        self.x += xstep
        self.y += ystep

    def show(self):
        stroke(0)
        point(self.x, self.y)

global walker

def setup():
    size(640, 240)
    background(255)

    global walker
    walker = Walker()

def draw():
    global walker
    walker.step()
    walker.show()


run()
