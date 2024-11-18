from p5 import *
import random

BALLOON_DIAMETER = 40

class Balloon:
    """Represents a Balloon.

    Attributes:
        position (Vector): The 2D coordinates of the Balloon.
        velocity (Vector): The 2D velocity of the Balloon in pixels per frame.
        acceleration (Vector): The 2D acceleration of the Balloon in pixels per
            frame squared.
    """
    def __init__(self):
        """Constructs a new Balloon at the center of the window."""
        self.position = Vector(width / 2, height / 2)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.diameter = BALLOON_DIAMETER
        self.radius = self.diameter / 2


    def apply_force(self, force: Vector):
        """Applies a force to the Balloon."""
        self.acceleration += force

    def check_edges(self):
        """Checks that the Balloon is in the window.

        Checks that the Balloon is in the window and updates its position and
        velocity if not.
        """
        if self.position.x < 0 + self.radius:
            self.position.x = 0 + self.radius
            self.velocity.x *= -1
        elif self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= -1

        if self.position.y < 0 + self.radius:
            self.position.y = 0 + self.radius
            self.velocity.y *= -1
        elif self.position.y > width - self.radius:
            self.position.y = width - self.radius
            self.velocity.y *= -1

    def step(self):
        """Updates the position of the Balloon."""
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0

    def show(self):
        """Draws the Balloon on the p5 canvas."""
        stroke(0)   # Black
        fill(140)   # Gray
        circle(self.position.x, self.position.y, self.diameter)


global balloon

def setup():
    """Setup the p5 canvas."""
    global balloon
    balloon = Balloon()

def draw():
    """Draw a single frame on the p5 canvas."""
    background(255)     # White

    # Pull in the balloon variable
    global balloon
    
    # Define the forces
    bouyancy = Vector(0, -0.1)
    wind = Vector(random.random() - 0.5, 0)

    # Apply the forces
    balloon.apply_force(bouyancy)
    balloon.apply_force(wind)

    # Update the balloon's position, check its edges, and draw it.
    balloon.step()
    balloon.check_edges()
    balloon.show()


# Run the p5 program
run()
