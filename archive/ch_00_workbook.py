from p5 import *
import random

class Walker:
    """Represents a generic walker.

    Attributes:
        x (int): The x-coordinate of the walker
        y (int): The y-coordinate of the walker
    """
    def __init__(self):
        """Initializes the Walker and locates it at the center of the screen"""
        self.x = width / 2      # width and height are p5 variables. Your IDE
        self.y = height / 2     # may not recognize them. It's ok.

    def show(self):
        """Draws the Walker on the p5 canvas"""
        stroke(0)   # Black
        point(self.x, self.y)

    def step(self):
        """Updates the x/y coordinates of the walker to step in a random 
        direction (or not at all)"""
        floor = -1      # Minimum step size
        ceiling = 1     # Maximum step size

        # Get step sizes for each dimension
        xstep = random.randint(floor, ceiling)
        ystep = random.randint(floor, ceiling)

        # Update the walker's location
        self.x += xstep
        self.y += ystep

# Initialize the walker
global walker

def setup():
    """Initializes the canvas"""

    # Set canvas size and background color
    size(640, 240)  # x, y
    background(255) # White

    # Pull in the global walker variable and initialize it to a new Walker
    global walker
    walker = Walker()

def draw():
    """Draw a frame"""

    # Pull in the global walker variable
    global walker

    # Update the position of the walker then draw it on the canvas
    walker.step()
    walker.show()

# Run the p5 program
run()
