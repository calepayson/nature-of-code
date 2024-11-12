from p5 import *

class Walker:
    """Represents a basic walker class

    Steps are calculated using perlin noise

    Attributes:
        x (int): The x coordinate of the walker
        y (int): The y coordinate of the walker
        tx (float): The time component to generate new positions along the x axis
        ty (float): The time component to generate new positions along the y axis
    """
    def __init__(self):
        """Creates a new Walker object"""
        # Define the time components to be used for perlin noise generation
        self.x = width / 2
        self.y = height / 2
        self.tx = 0
        self.ty = 10000

    def step(self):
        """Update the position of the walker

        Uses perlin noise to generate new positions.
        """
        xstep = remap(noise(self.tx), (0, 1), (-2, 2))
        ystep = remap(noise(self.ty), (0, 1), (-2, 2))

        self.x += xstep
        self.y += ystep

        # Increment the time components
        self.tx += 0.01
        self.ty += 0.01

    def show(self):
        """Draw a frame of the walker on the p5 canvas"""
        stroke(0)   # Black
        fill(50)    # Dark gray
        circle(self.x, self.y, 42)  # x, y, size

# Initialize a global walker variable
global walker

def setup():
    """Setup the p5 canvas"""
    # Define default canvas size and color
    size(640, 240)
    background(255)

    # Pull in the global walker variable and set it equal to a new Walker
    global walker
    walker = Walker()

def draw():
    """Draw a single frame on the canvas"""

    # Grab the walker, update its position, and draw it on the canvas
    global walker
    walker.step()
    walker.show()


# Run the p5 program
run()
