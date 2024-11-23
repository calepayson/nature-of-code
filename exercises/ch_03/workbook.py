from p5 import *
from objects import Mover
import random


# Adjust the mass of the mouse
MOUSE_MASS = 5

# Adjust the min and max gravitational force (for asthetic reasons).
MIN_GRAVITY = 2
MAX_GRAVITY = 25

# Adjust how much velocity is retained upon contact with the wall
BOUNCE_COEFFICIENT = 0.9

position = Vector(width / 2, height / 2)
mass = 2.5
mover = Mover(position, mass)

def draw():
    global mover

    background(255)

    mouse = Vector(mouse_x, mouse_y)
    direction = mouse - mover.position
    magnitude = (MOUSE_MASS * mover.mass) / (direction.mag() ** 2)
    direction.normalize()
    gravity = constrain(magnitude, MIN_GRAVITY, MAX_GRAVITY) * direction
    
    mover.apply_force(gravity)
    
    mover.update()
    mover.check_edges(BOUNCE_COEFFICIENT)
    mover.show()

run()
