from p5 import *
from objects import Mover, Attractor
import random

# Adjust the number of movers
NUMBER_OF_MOVERS = 4

# Adjust the attractor's mass
ATTRACTOR_MASS = 20

# Adjust the minimum and maximum size of movers
MIN_SIZE = 10
MAX_SIZE = 70

# Adjust the gravity constant
GRAVITY_CONSTANT = 1

# Adjust the expected screen width and height (p5 sets up before the screen 
# resizes)
SYSTEM_WIDTH = 930
SYSTEM_HEIGHT = 500


global attractor
movers = []

def setup():
    """Setup the p5 canvas."""
    # Pull in the global movers array and attractor variable
    global movers, attractor

    # Initialize the attractor
    center = Vector(SYSTEM_WIDTH / 2, SYSTEM_HEIGHT / 2)
    mass = ATTRACTOR_MASS
    attractor = Attractor(center, mass)

    # Initialize each mover
    for _ in range(NUMBER_OF_MOVERS):
        position = Vector(random.randint(0, SYSTEM_WIDTH), random.randint(0, SYSTEM_HEIGHT))
        size = random.randint(MIN_SIZE, MAX_SIZE)
        mover = Mover(position, size)
        movers.append(mover)

def draw():
    # Pull in the global movers array and attractor variable
    global movers, attractor

    # Erase the canvas
    background(255)     # White

    # Draw the attractor
    attractor.show()

    for mover in movers:
        force = attractor.attract(mover)
        mover.apply_force(force * GRAVITY_CONSTANT)

        mover.step()
        mover.check_edges(0.9)
        mover.show()


# Run the p5 program
run()
