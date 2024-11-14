from p5 import *

class Walker:
    """Represents a basic walker class

    Steps are calculated using perlin noise

    Attributes:
        position (Vector): The 2d coordinates of the Walker.
        velocity (Vecotr): The velocity of the Walker in pixles per frame.
        time (Vector): The time components used to calculate perlin noise.
    """
    def __init__(self):
        """Creates a new Walker object"""
        # Define the time components to be used for perlin noise generation
        self.position = Vector(width / 2, height / 2)
        self.velocity = Vector(0, 0)
        self.time = Vector(0, 10000)
        self.diameter = 48
        self.radius = self.diameter / 2

    def step(self):
        """Update the position of the walker

        Uses perlin noise to generate new positions.
        """
        self.velocity = Vector(
            remap(noise(self.time.x), (0, 1), (-5, 5)),
            remap(noise(self.time.y), (0, 1), (-5, 5))
        )

        self.position += self.velocity

        # Increment the time components
        self.time.x += 0.01
        self.time.y += 0.01

    def check_edges(self):
        """Checks the edges of the ball.

        If any part of the ball is outside the window, resets the ball to the
        edge and reverses the appropriate velocity dimension.
        """

        # Check and correct horizontal edges
        if self.position.x < 0 + self.radius:
            self.position.x = 0 + self.radius
            self.velocity.x *= -1   # Simulates a bounce
        elif self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= -1
        
        # Check and correct vertical edges
        if self.position.y < 0 + self.radius:
            self.position.y = 0 + self.radius
            self.velocity.y *= -1
        elif self.position.y > height - self.radius:
            self.position.y = height - self.radius
            self.velocity.y *= -1

    def show(self):
        """Draw a frame of the walker on the p5 canvas"""
        stroke(0)   # Black
        fill(128)    # Dark gray
        circle(self.position.x, self.position.y, self.diameter)  # x, y, size

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
    background(255)

    # Grab the walker, update its position, and draw it on the canvas
    global walker
    walker.step()
    walker.check_edges()
    walker.show()


# Run the p5 program
run()
