from p5 import *

ACCELERATION_RATE = 0.1

ROTATION_RATE = 0.05

class Rocket:
    """
    A generic Rocket object.

    The Rocket can have a force or a rotation applied to it.

    Attributes:
        position (Vector): The 2D coordinates of the Rocket.
        velocity (Vector): The 2D velocity of the Rocket in pixels per frame.
        Acceleration (Vector): The 2D acceleration of the Rockt in pixels per
            frame squared.
        angle (float): The direction the rocket is pointing towards in radians.
    """
    def __init__(self):
        """
        Construct a new Rocket.

        Centers the rocket within the window.
        """
        self.position = Vector(width / 2, height / 2)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.angle = 0

    def apply_rotation(self, theta: float):
        """
        Adds theta to the angle of the rocket.

        Args:
            theta (float): The desired change to the Rocket's angle in radians.
        """
        self.angle += theta

    def apply_force(self, force: Vector):
        """
        Adds the force to the rockets acceleration.

        Args:
            force (Vector): A 2D force acting on the Rocket.
        """
        self.acceleration += force


    def update(self):
        """
        Update the position of the Rocket.

        Notes:
            - Update resets acceleration.
        """
        # Update the Rocket's position
        self.velocity += self.acceleration
        self.position += self.velocity

        self.position.x %= width
        self.position.y %= height

        # Reset acceleration
        self.acceleration *= 0

    def show(self):
        """
        Draw the Rocket on the p5 canvas.
        """
        stroke(0)   # Black
        fill(127)   # Gray

        # Save the state of the p5 canvas
        push()

        # Set the origin to the center of the rocket
        translate(self.position.x, self.position.y)

        # Rotate around the origin 
        rotate(self.angle)

        # Draw the body
        tri_1 = Vector(0, -30)
        tri_2 = Vector(-15, 10)
        tri_3 = Vector(15, 10)
        triangle(tri_1.x, tri_1.y, tri_2.x, tri_2.y, tri_3.x, tri_3.y)

        if key == "UP":
            fill("red")

        # Draw the thrusters
        thruster_size = 5
        squ_1 = Vector(-10, 10)
        squ_2 = Vector(5, 10)
        square(squ_1.x, squ_1.y, thruster_size)
        square(squ_2.x, squ_2.y, thruster_size)

        # Revert back to the saved state of the p5 canvas
        pop()


# Initialize a new global Rocket object
rocket = Rocket()

def draw():
    """
    Draw a single frame on the p5 canvas.
    """
    # Pull in the global Rocket object
    global rocket

    # Reset the canvas
    background(255) # White

    # Apply forces based on user input
    if key == "UP":
        direction = Vector.from_angle(rocket.angle - (PI / 2))
        force = direction * ACCELERATION_RATE
        rocket.apply_force(force)
    if key == "RIGHT":
        rotation = ROTATION_RATE
        rocket.apply_rotation(rotation)
    if key == "LEFT":
        rotation = -1 * ROTATION_RATE
        rocket.apply_rotation(rotation)

    # Update the Rocket's position
    rocket.update()

    # Draw the Rocket
    rocket.show()


# Run the p5 program
run()
