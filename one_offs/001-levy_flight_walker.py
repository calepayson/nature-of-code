from p5 import *
import random

class Walker:
    """A generic walker object

    Step size is determined by the Levy flight variation of a random walk

    Attributes:
        x (int): The x coordinate of the walker
        y (int): The y coordinate of the walker
    """
    def __init__(self):
        """Creates a new Walker positioned in the center of the window"""
        self.x = width / 2
        self.y = width /2

    def step(self):
        """Updates the walkers coordinates using a Levy walk algorithm"""
        probability = random.random()

        if probability < 0.01:
            xstep = random.randint(-100, 100)
            ystep = random.randint(-100, 100)
        else:
            xstep = random.randint(-1, 1)
            ystep = random.randint(-1, 1)

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
