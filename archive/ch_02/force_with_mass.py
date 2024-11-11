from p5 import *
import random

class Mover():
    def __init__(self):
        self.position = Vector(random.randrange(0, width), random.randrange(0, height))
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.mass = 10

    def apply_force(self, force: Vector):
        self.acceleration += force / self.mass
    def reset_force(self):
        self.acceleration *= 0

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        if self.position.x <= 0 or self.position.x >= width:
            self.velocity.x *= -1
        if self.position.y <= 0 or self.position.y >= height:
            self.velocity.y *= -1

    def draw(self):
        stroke(0)
        fill(140)
        circle(self.position.x, self.position.y, 48)

global mover, gravity
gravity = Vector(0, 0.1)

def setup():
    size(640, 240)


    global mover, gravity
    mover = Mover()
    mover.apply_force(gravity)
    

def draw():
    background(255)

    wind = Vector(0.1, 0)

    global mover, gravity
    if (mouse_is_pressed):
        mover.apply_force(wind)
    else:
        mover.reset_force()
        mover.apply_force(gravity)

    mover.update()
    mover.draw()


run()
