from p5 import *

WIDTH = 640
HEIGHT = 240

def map(n, end):
    return n * end

class Walker:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.tx = 0
        self.ty = 10000

    def show(self):
        stroke(0)
        ellipse(self.x, self.y, 16, 16)

    def step(self):
        self.x = map(noise(self.tx), WIDTH)
        self.y = map(noise(self.ty), WIDTH)
        self.tx += 0.01
        self.ty += 0.01

walker = Walker()

def setup():
    size(WIDTH, HEIGHT)
    background(204)

def draw():
    walker.step()
    walker.show()

run()
