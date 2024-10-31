from p5 import *

class Mover:
    def __init__(self, x=320, y=120, mass=1):
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.mass = mass
        self.diameter = self.mass * 16
        self.radius = self.diameter / 2

    def apply_force(self, force: Vector):
        f = force / self.mass
        self.acceleration += f

    def apply_gravity(self):
        gravity = Vector(0, 0.1)
        self.apply_force(gravity * self.mass)

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

    def show(self):
        stroke(0)
        fill(175)
        circle(self.position.x, self.position.y, self.diameter)

    def check_edges(self):
        if self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= -1
        elif self.position.x < 0 + self.radius:
            self.position.x = 0 + self.radius
            self.velocity.x *= -1

        if self.position.y > height - self.radius:
            self.position.y = height - self.radius
            self.velocity.y *= -1
        elif self.position.y < 0 + self.radius:
            self.position.y = 0 + self.radius
            self.velocity.y *=-1

movers = []

def setup():
    size(640, 240)
    global movers
    mover1 = Mover(100, 30, 10)
    mover2 = Mover(400, 30, 2)
    movers.append(mover1)
    movers.append(mover2)

def draw():
    background(255)
    global movers

    wind = Vector(0.1, 0)

    for mover in movers:
        mover.apply_gravity()

        if mouse_is_pressed:
            mover.apply_force(wind)

        mover.update()
        mover.check_edges()
        mover.show()

run()
