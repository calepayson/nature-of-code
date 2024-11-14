from p5 import *
import random


class Walker:
    """Represents a random walker

    The walker has a 50% chance of taking a step in any direction and a 50%
    chance of thaking a step in the direction of the mouse

    Attributes:
        position (Vector): Represents the x and y coordinates of the walker.
        velocity (Vector): Represents the velocity of the walker in pixels per frame.
    """
    def __init__(self):
        """Initializes the Walker"""
        self.position = Vector(width / 2, height / 2)
        self.velocity = Vector(0, 0)

    def step(self):
        """Updates the position of the Walker

        - 50% of the time it steps 1 pixel in a random direction.
        - 50% of the time it steps 1 pixel in the direction of the mouse
        """
        random_number = random.random()

        # 50% of the time:
        if random_number < 0.5:
            # Step in a random direction
            self.velocity = Vector(random.randint(-1, 1), random.randint(-1, 1))
        # The other 50% of the time... step towards the mouse
        else:
            self.velocity = Vector(0, 0)
            if mouse_x > self.position.x:
                self.velocity.x = 1
            elif mouse_x < self.position.x:
                self.velocity.x = -1
            if mouse_y > self.position.y:
                self.velocity.y = 1
            elif mouse_y < self.position.y:
                self.velocity.y = -1

        # Update the position
        self.position += self.velocity

    def show(self):
        """Draw a frame of the walker"""
        stroke(0)   # Black
        # Draw a point
        point(self.position.x, self.position.y) 

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
