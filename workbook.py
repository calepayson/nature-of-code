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
        self.x = width / 2
        self.y = height / 2

    def show(self):
        """Draws the Walker on the p5 canvas"""
        stroke(0)
        point(self.x, self.y)

    def step(self):
        """Updates the x/y coordinates of the walker to step in a random 
        direction"""
        choice = random.randint(0,3)
        if choice == 0:
            self.x += 1
        elif choice == 1:
            self.x -= 1
        elif choice == 2:
            self.y += 1
        elif choice == 3:
            self.y -= 1

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
