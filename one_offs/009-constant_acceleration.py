from p5 import *

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

    def add_force(self, force: Vector):
        """ Add a force to the Ball

        Adds the force to the acceleration attribute.

        Args:
            force (Vector): A vector representing the new force
        """
        self.acceleration += force

    def step(self):
        """Updates the position of the Ball"""
        self.velocity += self.acceleration
        self.position += self.velocity

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
        """Draws the ball"""
        stroke(0)   # Black
        fill(127)   # Gray
        circle(self.position.x, self.position.y, self.diameter)


# Initialize a global ball variable (p5 functions don't take variables)
global ball

def setup():
    """Setup the p5 canvas"""
    # A vector representing the center of the screen
    position = Vector(width / 2, height / 2)
    # A random velocity
    velocity = Vector(2, 3)

    # Pull in the global ball variable and set it equal to a new Ball object
    global ball
    ball = Ball(position, 48)
    
    # Add a force to the ball
    force = Vector(0.001, 0.01)
    ball.add_force(force)

def draw():
    """Draw a single frame on the p5 canvas"""
    # Erase the previous canvas
    background(255)     # White

    # Pull in the ball variable, update its position, check its edges, and draw it
    global ball
    ball.step()
    ball.check_edges()
    ball.show()


# Run the p5 program
run()
