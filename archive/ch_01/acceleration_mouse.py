from p5 import *
import random

ACCELERATION = 0.001
NUMBER_OF_MOVERS = 3

class Mover():
    def __init__(self):
        self.position = Vector(random.randrange(0, width), random.randrange(0, height))
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

    def update_acceleration(self):
        mouse = Vector(mouse_x, mouse_y)
        line = mouse - self.position
        self.acceleration = line * ACCELERATION

    def update(self):
        self.update_acceleration()
        self.velocity += self.acceleration
        self.position += self.velocity
        self.velocity *= 0.99

    def show(self):
        stroke(0)
        fill(140)
        circle(self.position.x, self.position.y, 48)

movers = []

def setup():
    size(640, 240)
    global movers
    for _ in range(NUMBER_OF_MOVERS):
        movers.append(Mover())

def draw():
    background(255)
    global movers
    for mover in movers:
        mover.update()
        mover.show()


run()
