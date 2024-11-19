from p5 import *
from objects import Mover, Liquid

global mover

def setup():
    """Setup the p5 canvas."""
    # Initialize the mover object
    global mover
    mover = Mover(Vector(width / 2, height / 2), 40)

def draw():
    # Pull in the global mover
    global mover

    # Make a liquid object (We do it here to get proper size)
    liquid = Liquid(0, height / 2, width, height / 2, 0.2)

    # Erase the canvas
    background(255)     # White

    # Apply gravity
    gravity = Vector(0, 0.5)
    mover.apply_force(gravity)

    # If the mover is in the liquid
    if liquid.contains(mover):
        # Calculate and apply the drage force
        drag_force = liquid.calculate_drag(mover)
        mover.apply_force(drag_force)

    # Draw the liquid
    liquid.show()

    # Update the mover's position, check its edges, and draw it.
    mover.step()
    mover.check_edges(0.9)
    mover.show()


# Run the p5 program
run()
