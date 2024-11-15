# Create a simulation of an object that accelerates when you press the up arrow
# and brakes when you press the down arrow.

from p5 import *

class SpaceFighter:
    """Represents a simple Space Fighter

    Can Accelerate forwards and backwards.

    Attributes:
        position (Vector): The x and y coordinates of the fighter.
        velocity (Vector): A 2d vector representing the velocity of the fighter
                           in pixels / frame.
        acceleration (Vector): A vector representing the acceleration of the
                               fighter in pixels / frame^2.
    """
    def __init__(self):
        """Constructs a new SpaceFighter"""
        self.position = Vector(width / 2, height / 2)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

    def add_force(self, force: Vector):
        """Adds a force that acts upon the space fighter.

        Args:
            force (Vector): A vector representing the force to be added.
        """
        self.acceleration += force

    def step(self):
        """Updates the position of the space fighter.

        NOTE: Resets acceleration. If you want the fighter to constantly
        accelerate you must add all relevant forces to the fighter before each
        step call.
        """
        self.velocity += self.acceleration
        self.position += self.velocity

        self.acceleration *= 0

    def show(self):
        """Draws a single frame of the fighter."""
        stroke(0)
        triangle(
            self.position.x, self.position.y,
            self.position.x - 20, self.position.y + 40,
            self.position.x + 20, self.position.y + 40
        )


# Construct a new SpaceFighter
space_fighter = SpaceFighter()

def draw():
    """Draw a single frame on the p5 canvas."""
    background(255)     # White

    # pull in the global space fighter variable
    global space_fighter

    # If the up or down keys are pressed accelerate the fighter in the
    # appropriate direction
    if key == "UP":
        space_fighter.add_force(Vector(0, -0.01))
    elif key == "DOWN":
        space_fighter.add_force(Vector(0, 0.01))
    
    # Update the position of the fighter and draw it on the canvas
    space_fighter.step()
    space_fighter.show()

# Run the p5 program
run()

