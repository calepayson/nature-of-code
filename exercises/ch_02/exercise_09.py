from p5 import *
from objects import Mover, Liquid
import random

# Adjust the number of movers
NUMBER_OF_MOVERS = 3

# Adjust the minimum and maximum size of movers
MIN_SIZE = 10
MAX_SIZE = 70

# Adjust the gravity constant
GRAVITY_CONSTANT = 0.1

# Adjust the viscosity of the liquid
VISCOSITY = 0.01

# Adjust the expected screen width and height (p5 sets up before the screen 
# resizes)
SYSTEM_WIDTH = 930
SYSTEM_HEIGHT = 500


# Initialize an array to store movers
movers = []

def setup():
    """Set up the p5 canvas."""
    # Pull in the global movers array
    global movers

    # Add movers to the array
    for _ in range(NUMBER_OF_MOVERS):
        position = Vector(random.randint(0, SYSTEM_WIDTH), SYSTEM_HEIGHT / 4)
        size = random.randint(MIN_SIZE, MAX_SIZE)
        mover = Mover(position, size)
        movers.append(mover)

def draw():
    """Draw a single frame on the p5 canvas."""
    # Pull in the global movers array
    global movers


    # Erase the canvas
    background(255)     # White

    # Draw the liquid
    liquid = Liquid(0, height / 2, width, height / 2, VISCOSITY)
    liquid.show()

    # For each mover...
    for mover in movers:
        # Add gravity
        gravity = Vector(0, GRAVITY_CONSTANT * mover.mass)
        mover.apply_force(gravity)

        # If the mover is in the liquid...
        if liquid.contains(mover):
            # Calculate and apply the drage force
            drag_force = liquid.calculate_drag(mover)
            mover.apply_force(drag_force)

        # Update its position, check its edges, and draw it
        mover.step()
        mover.check_edges(0.9)
        mover.show()


# Run the p5 program
run()
