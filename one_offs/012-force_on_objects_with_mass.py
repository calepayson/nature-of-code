from p5 import *
import random

# Adjust the number of balls
NUMBER_OF_BALLS = 3

# Adjust the min and max size of balls
MIN_SIZE = 10
MAX_SIZE = 80

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

    # Initialize forces
    gravity = Vector(0, 0.5)
    wind = Vector((random.random() - 0.5) * 3, 0)

    for ball in balls:
        # Apply forces
        ball.add_force(gravity)
        ball.add_force(wind)

        # Update the position of the ball, check its edges, and draw it.
        ball.step()
        ball.check_edges()
        ball.show()


# Run the p5 program
run()
