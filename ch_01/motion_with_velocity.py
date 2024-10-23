from p5 import *
import random

class Mover:
    def __init__(self):
        self.position = Vector(random.randrange(0, width), random.randrange(0, height))
        self.velocity = Vector(random.random() - 0.5, random.random() - 0.5) * 4

    def update(self):
        self.position += self.velocity
        self.position.x %= width
        self.position.y %= height

    def show(self):
        stroke(0)
        fill(175)
        circle(self.position.x, self.position.y, 48)

global mover1, mover2

def setup():
    size(640, 240)
    global mover1, mover2
    mover1 = Mover()
    mover2 = Mover()

def draw():
    global mover
    mover1.update()
    mover2.update()
    mover1.show()
    mover2.show()

run()
