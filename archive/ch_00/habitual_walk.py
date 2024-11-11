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
        rng = random.random()
        
        if rng < .2:
            self.y += 1
        elif rng < .4:
            self.y -= 1
        elif rng < .6:
            self.x -= 1
        else:
            self.x += 1

walker = Walker(WIDTH, HEIGHT)

def setup():
    size(WIDTH, HEIGHT)
    background(255)
    walker.show()

def draw():
    walker.step()
    walker.show()

if __name__ == "__main__":
    run()
