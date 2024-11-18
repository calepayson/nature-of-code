from p5 import *
import random
import math

# Adjust the number of balls
NUMBER_OF_BALLS = 3

# Adjust the min and max size of balls
MIN_SIZE = 10
MAX_SIZE = 80

# Adjust repellence strength
REPELLENCE = 1

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

    def add_force(self, force: Vector):
        """ Add a force to the Ball

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

    def check_edges(self):
        """Check distance form edge and apply a force based on that."""

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


balls = []

def setup():
    """Setup the p5 canvas"""
    global balls

    for _ in range(NUMBER_OF_BALLS):
        # Get the position and size of the ball
        position = Vector(random.randrange(0, width), random.randrange(0, height))
        size = random.randrange(MIN_SIZE, MAX_SIZE)
        
        # Create a new ball and add it to the global list
        ball = Ball(position, size)
        balls.append(ball)

def draw():
    background(255)     # White
    
    global balls

    for ball in balls:
        # Calculate repellence
        x_distance = (width / 2) - ball.position.x
        y_distance = (height / 2) - ball.position.y

        repellence = REPELLENCE * Vector(x_distance / width, y_distance / height)

        # Apply force
        ball.add_force(repellence)

        # Update the position of the ball, check its edges, and draw it.
        ball.step()
        ball.check_edges()
        ball.show()


# Run the p5 program
run()