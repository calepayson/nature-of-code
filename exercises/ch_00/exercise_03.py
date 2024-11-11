from p5 import *
import random


class Walker:
    """Represents a random walker

    The walker has a 50% chance of taking a step in any direction and a 50%
    chance of thaking a step in the direction of the mouse

    Attributes:
        x (int): The x coordinate of the walker
        y (int): The y coordinate of the walker
    """
    def __init__(self):
        """Initializes the Walker"""
        self.x = width / 2      # width and height are p5 environment variables
        self.y = height / 2     # representing the dimensions of the window

    def step(self):
        """Updates the position of the Walker

        - 50% of the time it steps 1 pixel in a random direction.
        - 50% of the time it steps 1 pixel in the direction of the mouse
        """
        random_number = random.random()
        xstep = 0
        ystep = 0

        # 50% of the time:
        if random_number < 0.5:
            # Step in a random direction
            xstep = random.randint(-1, 1)
            ystep = random.randint(-1, 1)
        # The other 50% of the time... step towards the mouse
        else:
            if mouse_x > self.x:
                xstep = 1
            elif mouse_x < self.x:
                xstep = -1
            if mouse_y > self.y:
                ystep = 1
            elif mouse_y < self.y:
                ystep = -1

        # Update the position
        self.x += xstep
        self.y += ystep

    def show(self):
        """Draw a frame of the walker"""
        stroke(0)   # Black
        # Draw a point
        point(self.x, self.y) 

# Initialize a global walker variable
global walker

def setup():
    """Setup the p5 canvas"""
    # Specify the initail size and color of the canvas
    size(640, 240)
    background(255)     # White

    # Grab the global walker variable and set it equal to a new Walker object
    global walker
    walker = Walker()

def draw():
    """Draw a single frame on the canvas"""

    # Grab the global Walker variable
    global walker

    # Update the Walker's position and draw it
    walker.step()
    walker.show()


# Run the p5 program
run()
