from p5 import *
import random

# Adjust the number of balls
NUMBER_OF_BALLS = 3

class Ball: 
    """Represents a ball that can bounce around the screen.

    Attributes:
        position (Vector): The position of the ball within the window.
        velocity (Vector): The velocity of the ball in pixels / frame.
        acceleration (Vector): The acceleration of the ball in pixels / frame.
        diameter (int): The diameter of the ball in pixels.
        radius (int): The radius of the ball in pixels.
    """
    def __init__(self, position: Vector, diameter: int):
        """Constructs a new ball object.

        Args:
            position (Vector): The position of the ball within the window.
            diameter (int): The diameter of the ball in pixels.

        Returns:
            Ball: A new Ball object
        """
        self.position = position
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.diameter = diameter
        self.radius = self.diameter / 2
        self.mass = diameter / 4

    def apply_force(self, force: Vector):
        """Apply a force to the Ball

        Adds the force divided by the mass attribute to the acceleration 
        attribute.

        Args:
            force (Vector): A vector representing the new force
        """
        self.acceleration += force / self.mass

    def step(self):
        """Updates the position of the Ball.

        NOTE: Clears acceleration when called. If you want to have constant
        acceleration, continually add any relevant forces in the draw function.
        """
        self.velocity += self.acceleration
        self.position += self.velocity

        # Reset acceleration
        self.acceleration *= 0

    def check_edges(self, bounce=1.0):
        """Checks the edges of the ball.

        If any part of the ball is outside the window, resets the ball to the
        edge and reverses the appropriate velocity dimension.

        Args:
            bounce (float): The percentage of velocity retained after contact
                with an edge.
        """
        # Reverse bounce to reverse velocity.
        bounce *= -1
        # Check and correct horizontal edges
        if self.position.x < 0 + self.radius:
            self.position.x = 0 + self.radius
            self.velocity.x *= bounce
        elif self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= bounce
        
        # Check and correct vertical edges
        if self.position.y < 0 + self.radius:
            self.position.y = 0 + self.radius
            self.velocity.y *= bounce
        elif self.position.y > height - self.radius:
            self.position.y = height - self.radius
            self.velocity.y *= bounce

    def contact_edge(self):
        """Returns true when the Ball is within one pixel of the bottom edge.
        """
        return (self.position.y > height - self.radius - 1)

    def show(self):
        """Draws the ball"""
        stroke(0)   # Black
        fill(127)   # Gray
        circle(self.position.x, self.position.y, self.diameter)

balls = []

def setup():
    """Initialize the p5 canvas"""
    global balls

    for ball in range(NUMBER_OF_BALLS):
        position = Vector(random.randint(0, width), random.randint(0, height))
        diameter = random.randint(20, 60)
        ball = Ball(position, diameter)
        balls.append(ball)

def draw():
    """Draw a single frame on the p5 canvas."""
    # Erase any previous drawings
    background(255)     # White

    # Pull in the global objects
    global balls

    for ball in balls:
        # Apply gravity
        gravity = Vector(0, 1)
        ball.apply_force(gravity)

        # Apply wind when mouse is pressed
        if mouse_is_pressed:
            wind = Vector(0.5, 0)
            ball.apply_force(wind)

        # If the ball is in contact with the edge calculate friction
        if ball.contact_edge():
            c = 0.1
            friction = ball.velocity
            friction *= -1
            friction.normalize()
            friction *= c
            ball.apply_force(friction)

        # Check the edges, update the position, and draw the ball
        ball.check_edges(0.9)
        ball.step()
        ball.show()


# Run the p5 program
run()
