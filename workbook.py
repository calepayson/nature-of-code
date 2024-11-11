from p5 import *
import random

class Walker:
    def __init__(self):
        self.x = width / 2
        self.y = height / 2

    def show(self):
        stroke(0)
        point(self.x, self.y)

    def step(self):
        choice = random.randint(0,3)
        if choice == 0:
            self.x += 1
        elif choice == 1:
            self.x -= 1
        elif choice == 2:
            self.y += 1
        elif choice == 3:
            self.y -= 1

global walker

def setup():
    size(640, 240)
    global walker
    walker = Walker()
    background(255)

def draw():
    global walker
    walker.step()
    walker.show()

run()
