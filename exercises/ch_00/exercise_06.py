from p5 import *
import random

def accept_reject(floor, ceiling):
    """Returns a random value within the specified range

    Uses an accept reject algorithm to find the value. The algorithm is more
    likely to return large values.

    Args:
        floor (int): The minimum desired value.
        ceiling (int): The maximum desired value.

    Returns:
        float: A random value
    """
    while True:
        # Pick two random values between 0 and 1
        r1 = random.random()
        r2 = random.random()

        # If the second value is less than the first value...
        if r2 < r1:
            # Return the first value adjusted to fit the range
            return (r1 * (ceiling - floor)) + floor

class Walker:
    """A generic walker object

    Step size is determined using an accept reject algorithm

    Attributes:
        x (int): The x coordinate of the walker
        y (int): The y coordinate of the walker
    """
    def __init__(self):
        """Creates a new Walker positioned in the center of the window"""
        self.x = width / 2
        self.y = width /2

    def step(self):
        """Updates the walkers coordinates using a accept reject algorithm"""
        xstep = accept_reject(-1, 1)
        ystep = accept_reject(-1, 1)

        self.x += xstep
        self.y += ystep

    def show(self):
        stroke(0)
        point(self.x, self.y)

global walker

def setup():
    """Initialize the p5 canvas"""

    # Set default window size and background color
    size(640, 240)
    background(255)

    # Pull in the global walker variable and set it to a new Walker object
    global walker
    walker = Walker()

def draw():
    """Draw a frame on the p5 canvas"""

    # Update the global walker variable and draw it on the canvas
    global walker
    walker.step()
    walker.show()


# Run the p5 program
run()
