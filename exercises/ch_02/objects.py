from p5 import *

class Mover:
    """Represents a generic mover that can bounce around the screen.

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
        self.mass = diameter / 16

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


class Liquid:
    """Represents a generic liquid.

    The liquid is displayed as a rectangle.

    Attributes:
        x (int): The x coordinate of the top left corner.
        y (int): The y coordinate of the top left corner.
        width (int): The width of the liquid.
        height (int): The height of the liquid.
        viscosity (float): The viscosity of the liquid (0-1).
    """
    def __init__(self, x, y, width, height, viscosity):
        """Constructs a new Liquid object

        Args:
            x (int): The x coordinate of the top left corner.
            y (int): The y coordinate of the top left corner.
            width (int): The width of the liquid.
            height (int): The height of the liquid.
            viscosity (float): The viscosity of the liquid (0-1).
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.viscosity = viscosity

    def contains(self, mover: Mover) -> bool:
        """Returns a boolean based on wether or not the mover is in the liquid."""
        within_x = mover.position.x > self.x and mover.position.x < self.x + self.width
        within_y = mover.position.y > self.y and mover.position.y < self.y + self.height
        return within_x and within_y

    def calculate_drag(self, mover: Mover) -> Vector:
        """Calculate the drag the liquid exerts on a mover.

        Limits the the drag to the magnitude of the Mover's acceleration. If 
        other forces are being applied, drag won't be calculated correctly.
        """
        speed = mover.velocity.mag()
        surface_area = mover.diameter

        # Calculate the magnitude of the drag force
        drag_magnitude = speed * speed * self.viscosity * surface_area

        # Calculate the direction of the drag force
        drag_direction = mover.velocity.copy() * -1
        drag_direction.normalize()

        # Calculate the drag force
        drag_force = float(drag_magnitude) * drag_direction
        drag_force.limit(upper_limit=mover.velocity.mag())
        return drag_force

    def show(self):
        """Draw the Liquid object."""
        no_stroke()
        fill(175)
        rect(self.x, self.y, self.width, self.height)

class Attractor:
    """Simulates an Attractor with a position and mass.

    Attributes:
        position (Vector): A 2D vector representing the Attractor's coordinates.
        mass (int): The mass of the Attractor.
    """
    def __init__(self, position: Vector, mass: int):
        """Construct a new Attractor object with the given attributes.

        Args:
            position (Vector): A 2D vector representing the Atrractor's desired
                coordinates.
            mass (int): The desired mass of the Attractor.
        """
        self.position = position
        self.mass = mass

    def show(self):
        """Draw the attractor."""
        stroke(0)       # Black
        fill(175, 200)  # Gray, Mostly transparent
        circle(self.position.x, self.position.y, self.mass * 2)

    def attract(self, mover: Mover):
        """Calculate the gravitational force exerted on a given mover."""
        force = self.position - mover.position
        distance = constrain(force.mag(), 5, 25)
        strength = float((self.mass * mover.mass) / (distance ** 2))
        force.normalize()
        force *= strength
        return force
