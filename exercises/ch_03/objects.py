from p5 import *

class Mover:
    """Represents a generic Mover.

    Attributes:
        position (Vector): The 2D coordinates of the Mover.
        velocity (Vector): A 2D vector representing the Mover's velocity in 
            pixels per frame.
        acceleration (Vector): A 2D vector representing the Mover's acceleration
            in pixels per frame squared.
        mass (int): The Mover's mass in generic units.
        diameter (int): The Mover's diameter in pixels.
        radius (int): The Mover's radius in pixels.
    """
    def __init__(self, position: Vector, mass: int):
        """Constructs a new Mover object.

        Args:
            position (Vector): The 2D coordinates of the Mover.
            mass (int): The mass of the Mover.
        """
        # Dynamic properties
        self.position = position
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

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
        """Update the position of the mover.

        This method also clears the acceleration attribute. Forces must be 
        applied on a frame by frame basis.
        """
        # Apply all forces and update the position
        self.velocity += self.acceleration
        self.position += self.velocity

        # Reset acceleration
        self.acceleration *= 0

    def show(self):
        """Draw the Mover."""
        stroke(0)   # Black
        fill(127)   # Gray
        circle(self.position.x, self.position.y, self.diameter)
