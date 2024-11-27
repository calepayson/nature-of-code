from p5 import *

# Hooke's Law:
# F = -k * x
# Where:
#   - F is the spring force.
#   - k is the spring constant.
#   - x is the distance from rest.



class Bob:
    def __init__(self):
        self.anchor = Vector(width / 2, 0)
        self.position = Vector(width / 2, 120)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

    def apply_force(self, force: Vector):
        self.acceleration += force

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity

        self.acceleration *= 0

    def show(self):
        stroke(0)
        fill(127)
        line(self.anchor.x, self.anchor.y, self.position.x, self.position.y)
        circle(self.position.x, self.position.y, 48)


bob = Bob()

def draw():
    global bob

    background(255)

    k = 0.1
    rest_length = 100

    direction = bob.position - bob.anchor
    current_length = direction.mag()
    direction.normalize()
    x = float(current_length - rest_length)
    force = -1 * k * x * direction

    bob.apply_force(force)

    bob.update()
    bob.show()

run()
