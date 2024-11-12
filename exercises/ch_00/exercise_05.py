from p5 import *
import random

class Walker:
    """Represents a Walker that takes steps based on a normal distribution
    Attributes:
        x (int): The x coordinate of the Walker
        y (int): The y coordinate of the Walker
    """
    def __init__(self):
        """Initialize the walker at a point in the center of the screen"""
        self.x = width / 2
        self.y = height / 2

    def step(self):
        """Update the postion of the Walker

        Uses a normal distribution to determine the step size/direction
        """

        # Get the step size/direction
        xstep = random.gauss(0, 2)
        ystep = random.gauss(0, 2)

        # Update the Walker's position
        self.x += xstep
        self.y += ystep

    def show(self):
        """Draw the walker on the p5 canvas"""
        stroke(0)   # Black
        point(self.x, self.y)

# Create a global walker variable
global walker

def setup():
    """Setup the p5 canvas"""
    # Set the initial canvas size and background color
    size(640, 240)
    background(255)

    # Set the global walker variable to a new walker
    global walker
    walker = Walker()

def draw():
    """Draw a single frame of the walker"""
    # Update the position of the global walker variable then draw it
    global walker
    walker.step()
    walker.show()


# Run the p5 program
run()
