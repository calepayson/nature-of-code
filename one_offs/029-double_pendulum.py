from p5 import *
import random

# Adjust gravity
GRAVITY = 0.4

class Pendulum:
    """
    Represents a simple pendulum.

    Attributes:
        pivot (Vector): The 2D coordinates of the pivot point.
        bob (Vector): The 2D coordinates of the bob.
        length (int): The length of the pendulum.
        angle (float): The angle between the pendulum and -pi/2.
        angle_velocity (float): The rate of change of the angle in pixels per
            frame.
        angle_acceleration (float): The rate of change of the angle_velocity in
            pixels per frame.
        damping (float): The percent of velocity retained each frame.
        bob_radius (int): The radius of the pendulum bob.
    """
    def __init__(self, pivot: Vector, length: int):
        """
        Construct a new Pendulum object.

        Args: 
            pivot (Vector): The 2D coordinates of the pendulums pivot.
            length (int): The length of the pendulum in pixels.
        """
        self.pivot = pivot
        self.bob = Vector(0, 0)
        self.length = length
        self.angle = 3 * PI / 4
        self.angle_velocity = 0
        self.angle_acceleration = 0
        self.damping = 0.999
        self.bob_radius = 10

    def update(self):
        """
        Update the position of the Pendulum's bob.
        """
        # Use Hooke's law to calculate the force
        self.angle_acceleration = (-1 * GRAVITY / self.length) * sin(self.angle)

        # Update the bob's position
        self.angle_velocity += self.angle_acceleration
        self.angle += self.angle_velocity

        # Dampen acceleration
        self.angle_velocity *= self.damping

    def update_pivot(self, pivot: Vector):
        """
        Update the coordinates of the Pendulum's pivot.

        Args:
            pivot (Vector): The new 2D coordinates of the Pendulum's pivot.
        """
        self.pivot = pivot


    def show(self):
        """
        Draw the Pendulum.
        """
        # Calculate the Bob's coordinates relative to the pivot
        self.bob = Vector(self.length * sin(self.angle), self.length * cos(self.angle))
        # Adjust the bob's coordinates to the global canvas
        self.bob += self.pivot

        # Reset the pallete
        stroke(0)
        fill(127)

        # Draw the Pendulum
        line(self.pivot.x, self.pivot.y, self.bob.x, self.bob.y)
        circle(self.bob.x, self.bob.y, self.bob_radius * 2)

# Create a new global pendulum object
pivot = Vector(width / 2 , height / 2)
pendulum_1 = Pendulum(pivot, 80)
pendulum_2 = Pendulum(pivot, 100)

def draw():
    """
    Draw a single frame on the p5 canvas.
    """
    # Pull in the global variable
    global pendulum_1, pendulum_2

    # Reset the canvas
    background(255)

    # Move pendulum_1 to the center of the screen
    center = Vector(width /  2, height / 2)
    pendulum_1.update_pivot(center)

    # Update pendulum_1's position and then draw it
    pendulum_1.update()
    pendulum_1.show()

    # Update pendulum_2's pivot and position then draw it
    pendulum_2.update_pivot(pendulum_1.bob)
    pendulum_2.update()
    pendulum_2.show()


# Run the p5 program
run()
