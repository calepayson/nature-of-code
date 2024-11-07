from p5 import *


# TIME_X = 0
# TIME_Y = 10000


class Mover:
    def __init__(self, x, y, size):
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.radius = size
        self.mass = size / 4 

    def apply_force(self, force: Vector):
        self.acceleration += force / self.mass

    def check_edges(self):
        if self.position.x < 0:
            self.position.x = 0
            self.velocity.x *= -1
        elif self.position.x > width:
            self.position.x = width
            self.velocity.x *= -1

        if self.position.y < 0:
            self.position.y = 0
            self.velocity.y *= -1
        elif self.position.y > height:
            self.position.y = height
            self.velocity.y *= -1

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

    def show(self):
        stroke(0)
        fill(144)
        circle(self.position.x, self.position.y, self.radius)

movers = []

def setup():
    size(640, 240)
    global movers

    movers.append(Mover(100, 100, 40))
    movers.append(Mover(300, 100, 80))

def draw():
    global movers

    background(255)

    gravity = Vector(0, 0.1)
    wind = Vector(0.1, 0)

    for mover in movers:
        mover.apply_force(gravity)

        if mouse_is_pressed:
            mover.apply_force(wind)

        if mover.position.y < height:
            magnetism = 1 / (height - mover.position.y)
            magnetic_force = Vector(0, -10 * magnetism)
            mover.apply_force(magnetic_force)

        mover.update()
        mover.check_edges()
        mover.show()

run()
