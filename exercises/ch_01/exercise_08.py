from p5 import *
import math

# Adjust the strength of gravity betwen objects
GRAVITY_CONSTANT = 0.01

# Adjust the mass of the mouse
MOUSE_MASS = 1000

class Ball:
    """Represents a generic Ball.

    This ball is attracted to the mouse.

    Attributes:
        position (Vector): The 2D coordinates of the Ball.
        velocity (Vector): The 2D velocity of the Ball in pixels per frame.
        acceleration (Vector): The 2D acceleration of the Ball in pixels per
                               frame squared.
        diameter (int): The diameter of the Ball in pixels.
        radius (float): The radius of the Ball in pixels.
        mass (int): The mass of the ball (proportional to diameter).
    """
    def __init__(self, position: Vector, diameter: int):
        """Constructs a new ball object.

        Args:
            position (Vector): The desired 2D coordinates of the Ball.
            diameter (int): The desired diameter of the Ball in pixels.

        Returns:
            Ball: A new Ball object with the specified attributes.
        """
        # Movement attributes
        self.position = position
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

        # Dimension attributes
        self.diameter = diameter
        self.radius = self.diameter / 2
        self.mass = 3 * (self.radius ** 2)

    def apply_force(self, force: Vector):
        """Adds a force to the Ball.

        Args:
            force (Vector): A 2D force
        """
        self.acceleration += force / self.mass

    def step(self):
        """Updates the position of the Ball."""
        self.velocity += self.acceleration
        self.position += self.velocity

        # Reset acceleration
        self.acceleration *= 0

    def show(self):
        """Draw the Ball on the canvas"""
        stroke(0)   # Black
        fill(140)   # Gray
        circle(self.position.x, self.position.y, self.diameter)

    def calculate_gravity(self, position_2: Vector, mass_2: int):
        """Calculates and adds a gravitational force to the Ball.

        The force is calculated from the given position and mass. The formula
        is G * (m1 * m2) / r. We use r instead of r squared for asthetic 
        reasons.

        Args:
            position_2 (Vector): The 2D coordinates of the second object.
            mass_2 (int): The mass of the second object.
        """
        direction = position_2 - self.position
        distance = math.ceil(direction.magnitude)   # Use math to prevent divide by zero
        force = GRAVITY_CONSTANT * (self.mass * mass_2) / (distance)
        direction.normalize()
        self.apply_force(force * direction)

    def add_gravity(self, other):
        """Adds a force representing the gravitational force exerted by another
        ball on this one.

        Args:
            other (Ball): The other ball object
        """
        self.calculate_gravity(other.position, other.mass)

    def add_mouse_gravity(self):
        """Adds a force representing the gravitational force exerted by the 
        mouse on this ball.
        """
        mouse = Vector(mouse_x, mouse_y)
        self.calculate_gravity(mouse, MOUSE_MASS)
        

# Initialize a new global variable
balls = []

def setup():
    """Setup the p5 canvas."""
    # Pull in the global variable
    global balls

    # Initialize two new balls
    ball_1 = Ball(Vector(300, 200), 24)
    ball_2 = Ball(Vector(400, 300), 32)

    # Push them to the global variable
    balls.append(ball_1)
    balls.append(ball_2)

def draw():
    """Draw a single frame on the p5 canvas."""
    background(255)     # White

    # Pull in the global ball variables
    global balls

    # For each ball object...
    for i in range(len(balls)):
        # Add the gravitational force of the mouse
        balls[i].add_mouse_gravity()

        # For every other ball...
        for j in range(len(balls)):
            if i != j:
                # Add the gravitational force of that ball to this one
                balls[i].add_gravity(balls[j])

        # Update the postion of the ball and draw it on the canvas
        balls[i].step()
        balls[i].show()


# Run the p5 program
run()
