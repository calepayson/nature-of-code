from p5 import *

class Mover:
    def __init__(self):
        self.position = Vector(width / 2, height / 2)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.time = 0

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity

        if 0 >= self.position.x or self.position.x >= width:
            self.velocity.x *= -1
        if 0 >= self.position.y or self.position.y >= height:
            self.velocity.y *= -1
        if self.position.x < 0: self.position.x = 0
        if self.position.x > width: self.position.x = width
        if self.position.y < 0: self.position.y = 0
        if self.position.y > height: self.position.y = height

        self.velocity *= 0.99 
        self.time += 0.01

    def show(self):
        stroke(0)
        fill(140)
        circle(self.position.x, self.position.y, 48)

    def apply_force(self, force: Vector):
        self.acceleration += force

    def reset_forces(self):
        self.acceleration *= 0

global mover

def setup():
    size(640, 240)
    global mover
    mover = Mover()
    float = Vector(0, -0.01)
    mover.apply_force(float)

def draw():
    background(255)
    global mover
    wind = Vector(
        (noise(mover.time) - 0.5) * 0.01,
        (noise(mover.time * 10000) - 0.5) * 0.2
    )
    mover.apply_force(wind)
    mover.update()
    mover.show()

run()
