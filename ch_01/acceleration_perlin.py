from p5 import *

class Mover:
    def __init__(self):
        self.tx = 0
        self.ty = 10000
        self.position = Vector(width / 2, height / 2)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

    def update(self):
        self.acceleration = Vector(noise(self.tx) - 0.5, noise(self.ty) - 0.5) * 0.01
        self.tx += 0.01
        self.ty += 0.01

        self.velocity += self.acceleration
        self.position += self.velocity
        
        self.position.x %= width
        self.position.y %= height

    def show(self):
        background(255)
        stroke(0)
        fill(140)
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
