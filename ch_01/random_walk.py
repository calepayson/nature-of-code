from p5 import *
import random

class Walker:
    def __init__(self, width, height):
        self.x = width / 2
        self.y = height / 2

    def show(self):
        stroke(0)
        point(self.x, self.y)

    def step(self):
        choice = floor(random.randint(0, 3));

        if choice == 0:
            self.x += 1
        elif choice == 1:
            self.x -= 1
        elif choice == 2:
            self.y += 1
        else:
            self.y -= 1

walker = Walker(640, 240)

def setup():
    size(640, 240)
    background(204)

def draw():
    walker.step()
    walker.show()

if __name__ == "__main__":
    run()

