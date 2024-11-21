from p5 import *

# Adjust the rate of angle acceleration
ANGLE_ACCELERATION_FACTOR = 0.1

# Adjust the min and max rotation speeds
MIN_ANGLE_VELOCITY = -0.1
MAX_ANGLE_VELOCITY = 0.1

class Mover:
    """Represents a generic Mover.

    Attributes:
        position (Vector): The 2D coordinates of the Mover.
        velocity (Vector): A 2D vector representing the Mover's velocity in 
            pixels per frame.
        acceleration (Vector): A 2D vector representing the Mover's acceleration
            in pixels per frame squared.
        angle (float): The angle of the Mover.
        angle_velocity (float): The rate of change of the Mover's angle in 
            radians per frame.
        angle_acceleration (float): The rate of change of the Mover's angle
            velocity in radians per frame.
        mass (float): The Mover's mass in generic units.
        diameter (float): The Mover's diameter in pixels.
        radius (float): The Mover's radius in pixels.
    """
    def __init__(self, position: Vector, mass: float):
        """Constructs a new Mover object.

        Args:
            position (Vector): The 2D coordinates of the Mover.
            mass (int): The mass of the Mover.
        """
        # Dynamic properties
        self.position = position
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.angle = 0
        self.angle_velocity = 0
        self.angle_acceleration = 0

        # Static properties
        self.mass = mass
        self.diameter = mass * 16
        self.radius = self.diameter / 2

    def apply_force(self, force: Vector):
        """Apply a force to the Mover.

        Divides the force by the movers mass then adds the resulting vector to
        the Mover's acceleration.
        """
        self.acceleration += force / self.mass

    def check_edges(self, energy_retention: float = 1.0):
        """Checks that the Mover is within the window.

        This method checks to see if any part of the Mover is outside the 
        window. If this is the case, it updates the Mover's position so that it
        is within the window and reverses the Mover's velocity along the 
        respective axis.

        Args:
            energy_retention (float): The percentage of energy retained by the 
                Mover when it bounces off an edge. Where 1 is equal to 100%.
                Defaults to 1.0.
        """
        # Calculate the velocity modifier.
        velocity_modifier = -1 * energy_retention

        # Check x axis
        if self.position.x < 0 + self.radius:
            self.position.x = 0 + self.radius
            self.velocity.x *= velocity_modifier
        elif self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= velocity_modifier
        
        # Check y axis
        if self.position.y < 0 + self.radius:
            self.position.y = 0 + self.radius
            self.velocity.y *= velocity_modifier
        elif self.position.y > height - self.radius:
            self.position.y = height - self.radius
            self.velocity.y *= velocity_modifier


    def update(self):
        """Update the position and angle of the Mover.

        This method also clears the acceleration attribute. Forces must be 
        applied on a frame by frame basis.
        """
        # Apply all forces
        self.velocity += self.acceleration
        self.position += self.velocity

        # Calculate angle acceleration
        self.angle_acceleration = self.acceleration.x * ANGLE_ACCELERATION_FACTOR
        # Calculate and constrain angle velocity
        self.angle_velocity += self.angle_acceleration
        self.angle_velocity = constrain(
                self.angle_velocity, 
                MIN_ANGLE_VELOCITY, 
                MAX_ANGLE_VELOCITY)
        # Update angle
        self.angle += self.angle_velocity

        # Reset acceleration
        self.acceleration *= 0

    def show(self):
        """Draw the Mover.

        Saves the state of the canvas, centers the origin on the mover and 
        rotates it, then restores the state of the canvas. If things start
        showing up in weird places this method is a likely culprit.
        """
        # Initialize the color pallet
        stroke(0)   # Black
        fill(127)   # Gray

        # Save current canvas state so rotation and translation doesn't effect
        # the global program
        push()

        # Set the origin to the Mover's position
        translate(self.position.x, self.position.y)

        # Rotate by the angle
        rotate(self.angle)

        # Draw the mover
        circle(0, 0, self.diameter)
        line(0, 0, self.radius, 0)  # To help keep track of rotation

        # Restore previous state of the p5 canvas
        pop()
