from p5 import *
import random

class Mover:
    def __init__(self):
        self.position = Vector(width / 2, height / 2)
        self.velocity = Vector(0, 0)

        random_num_1 = random.random() - 0.5
        random_num_2 = random.random() - 0.5
        self.acceleration = Vector(random_num_1, random_num_2)

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.position.x %= width
        self.position.y %= height

    def show(self):
        stroke(0)
        fill(200)
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
