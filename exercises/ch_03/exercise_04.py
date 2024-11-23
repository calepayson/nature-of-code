from p5 import *

# Adjust the rate of acceleration
ACCELERATION = 0.01

class SpaceShip:
    """
    Represents a space ship.

    Attributes:
        position (Vector): The 2D coordinates of the spaceship.
        velocity (Vector): The 2D velocity of the spaceship in pixels per frame.
        acceleration (Vector): The 2D acceleration of the spaceship in pixels
            per frame squared.
    """
    def __init__(self):
        """
        Construct a new SpaceShip object.

        Constructs a new SpaceShip object positioned that is positioned in the
        center of the screen and has no velocity or acceleration.
        """
        self.position = Vector(width / 2, height / 2)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

    def apply_force(self, force: Vector):
        """
        Apply a force to the SpaceShip.

        Typically used to simulate acceleration.

        Args:
            force (Vector): A vector representing the direction of force.
        """
        self.acceleration += force

    def update(self):
        """
        Update the position of the SpaceShip.

        Resets acceleration to 0. If you want to apply continuous acceleration
        you must reapply all forces after every update call.
        """
        self.velocity += self.acceleration
        self.position += self.velocity

        self.acceleration *= 0

    def show(self):
        """
        Draw the SpaceShip.
        """
        # Calculate the direction of travel
        angle = atan2(self.velocity.y, self.velocity.x) - (PI / 2)

        # Set the color pallete
        stroke(0)   # Black
        fill(127)   # Gray

        # Rotate the spaceship and draw it
        push()
        translate(self.position.x, self.position.y)
        rotate(angle)
        triangle(0, 0, -5, -20, 5, -20)
        pop()
        

# Initialize a new global SpaceShip
space_ship = SpaceShip()

def draw():
    """
    Draw a single frame on the p5 canvas.
    """
    # Pull in the global space_ship variable (necessary in p5)
    global space_ship

    # Reset the canvas
    background(255) # White

    # Initialize a force vector
    force = Vector(0, 0)

    # Handle user input
    if key == "UP":
        force = Vector(0, -1 * ACCELERATION)
    elif key == "RIGHT":
        force = Vector(ACCELERATION, 0)
    elif key == "DOWN":
        force = Vector(0, ACCELERATION)
    elif key == "LEFT":
        force = Vector(-1 * ACCELERATION, 0)

    # Apply the force
    space_ship.apply_force(force)

    # Update the space_ship's position
    space_ship.update()

    # Draw the space_ship
    space_ship.show()


# Run the p5 program
run()
