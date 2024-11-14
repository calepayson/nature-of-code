from p5 import *

class Ball: 
    """Represents a ball that can bounce around the screen.

    Attributes:
        position (Vector): The position of the ball within the window.
        velocity (Vector): The velocity of the ball.
        diameter (int): The diameter of the ball in pixels.
        radius (int): The radius of the ball in pixels.
    """
    def __init__(self, position: Vector, velocity: Vector, diameter: int):
        """Constructs a new ball object.

        Args:
            position (Vector): The position of the ball within the window.
            velocity (Vector): The velocity of the ball in pixels / frame.
            diameter (int): The diameter of the ball in pixels.

        Returns:
            Ball: A new Ball object
        """
        self.position = position
        self.velocity = velocity
        self.diameter = diameter
        self.radius = self.diameter / 2

    def step(self):
        """Updates the position of the Ball"""
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
    ball = Ball(position, velocity, 48)

def draw():
    """Draw a single frame on the p5 canvas"""
    # Pull in the ball variable, update its position, check its edges, and draw it
    global ball
    ball.step()
    ball.check_edges()
    ball.show()


# Run the p5 program
run()
