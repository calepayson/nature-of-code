from p5 import *

class Mover:
    def __init__(self):
        self.position = Vector(width, height) / 2
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

    def correct_overflow(self):
        self.position.x %= width
        self.position.y %= height

    def update(self):
        self.acceleration = Vector.random_2D()
        self.velocity += self.acceleration
        self.position += self.velocity
        self.correct_overflow()

    def show(self):
        stroke(0)
        circle(self.position.x, self.position.y, 48)

global mover

def setup():
    size(640, 240)
    global mover
    mover = Mover()

def draw():
    global mover
    mover.update()
    mover.show()

run()
