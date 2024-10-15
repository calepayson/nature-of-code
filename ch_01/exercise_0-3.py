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

    def rand_step(self):
        xstep = random.randint(-1, 1)
        ystep = random.randint(-1, 1)

        self.x += xstep
        self.y += ystep

    def mouse_step(self):
        if self.x < mouse_x:
            self.x += 2
        else: 
            self.x -= 2

        if self.y < mouse_y:
            self.y += 2
        else:
            self.y -= 2

    def step(self):
        rng = random.random()
        if rng < .5:
            self.rand_step()
        else:
            self.mouse_step()

walker = Walker()

def setup():
    size(WIDTH, HEIGHT)
    background(244)

def draw():
    walker.step()
    walker.show()

run()

