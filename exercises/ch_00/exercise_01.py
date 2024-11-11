from p5 import *
import random

class Walker:
    """Represents a Walker

    A walker is a point drawn on a p5 canvas that can move over time. This 
    walker has a tendency to walk down and to the right.

    Attributes:
        x (int): The x coordinate of the walker
        y (int): The y coordinate of the walker
    """
    def __init__(self):
        """Initializes the walker and centers it on the canvas"""
        self.x = width / 2
        self.y = height / 2

    def step(self):
        """Update the position of the walker"""
        xstep = random.randint(-1, 2)   
        ystep = random.randint(-1, 2)

        self.x += xstep
        self.y += ystep

    def show(self):
        """Draws the walker on the canvas"""
        stroke(0)
        point(self.x, self.y)


# Initialize a global walker variable
global walker

def setup():
    """Set up the canvas"""

    # Set canvas size and background color
    size(640, 240)
    background(255)     # Black

    # Pull in the global walker variable and initialize it to a new walker
    global walker
    walker = Walker()

def draw():
    """Draw a single frame on the p5 canvas"""

    # Pull in the global walker variable
    global walker

    # Update the walker's position then draw it on the canvas
    walker.step()
    walker.show()

# Run the p5 program
run()
