from p5 import *

class Ball:
    """Represents a generic Ball object.

    Args:
        position (Vector): The x and y coordinates of the ball.
        velocity (Vector): The 2D velocity of the ball in pixels / frame.
        acceleration (Vector): The 2D acceleration of the ball in pixels per
                               frame squared.
        diameter (int): The diameter of the ball.
        radius (float): The radius of the ball.
        time (Vector): A vector representing 2D time. Used for calculating 
                       perlin noise.
    """
    def __init__(self, position: Vector, diameter: int):
        """Constructs a new ball object.

        Args:
            position (Vector): The 2D coordinates of the ball.
            diamater (Vector): The desired diameter of the ball.
        """
        self.position = position
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        self.diameter = diameter
        self.radius = self.diameter / 2
        self.time = Vector(0, 10000)

    def add_force(self, force: Vector):
        """Adds a force to the Ball object."""
        self.acceleration += force

    def use_noise(self):
        """Uses perlin noise to add a random force to the Ball object."""
        # Get random forces and add them to the Ball object
        x_accel = remap(noise(self.time.x), (0, 1), (-1, 1))
        y_accel = remap(noise(self.time.y), (0, 1), (-1, 1))
        self.add_force(Vector(x_accel, y_accel))

        # Update time
        self.time.x += 0.01
        self.time.y += 0.01

    def step(self):
        """Updates the position of the Ball.

        NOTE: Resets acceleration when called. To simulate a constant force 
        make sure to add the relevant forces before each step call.
        """
        self.velocity += self.acceleration
        self.position += self.velocity

        # Reset acceleration
        self.acceleration *= 0

    def check_edges(self):
        """Checks that the ball is within the window and updates its position
        if not.
        """
        # Check the x dimension
        if self.position.x < 0 + self.radius:
            self.position.x = 0 + self.radius
            self.velocity.x *= -1
        elif self.position.x > width - self.radius:
            self.position.x = width - self.radius
            self.velocity.x *= -1

        # Check the y dimension
        if self.position.y < 0 + self.radius:
            self.position.y = 0 + self.radius
            self.velocity.y *= -1
        elif self.position.y > height - self.radius:
            self.position.y = height - self.radius
            self.velocity.y *= -1

    def show(self):
        """Draws a ball on a p5 canvas."""
        stroke(0)   # Black
        fill(140)   # Gray
        circle(self.position.x, self.position.y, self.diameter)

# Set initial variables for the ball
initial_position = Vector(width / 2, height / 2)
size = 48

# Initialize a new global Ball
ball = Ball(initial_position, size)

def draw():
    """Draw a single frame on the p5 canvas."""
    background(255)     # White

    # Pull in the global ball variable
    global ball

    # Apply a random force to the ball, update its position, check that it is
    # in the window, and then draw it.
    ball.use_noise()
    ball.step()
    ball.check_edges()
    ball.show()


# Run the p5 program
run()
