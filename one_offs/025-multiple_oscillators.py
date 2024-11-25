from p5 import *
import random


# Adjust the number of oscillators
NUMBER_OF_OSCILLATORS = 4


class Oscillator:
    """
    Represents an object that oscillates around the origin in two dimensions.

    Attributes:
        angle (Vector): The x and y coordinates of the Oscillator's unit vector.
        angle_velocity (Vector): The change in the Oscillator's angle per frame.
        amplitude (Vector): The amplitude of each angle's oscillation.
    """
    def __init__(self):
        """
        Construct a new Oscillator in the center of the canvas.
        """
        self.angle = Vector(0, 0)
        self.angle_velocity = Vector(
            (random.random() - 0.5) * 0.1, 
            (random.random() - 0.5) * 0.1)
        self.amplitude = Vector(
            random.randint(20, width / 2), 
            random.randint(20, height / 2))

    def update(self):
        """
        Update the position of the Oscillator.
        """
        self.angle += self.angle_velocity

    def show(self):
        """
        Draw the Oscillator.
        """
        # Calculate the x and y coordinates
        x = sin(self.angle.x) * self.amplitude.x
        y = sin(self.angle.y) * self.amplitude.y

        # Save the current state of the p5 canvas
        push()

        # Update the state of the p5 canvas to have the origin in the center of
        # the screen
        translate(width / 2, height / 2)

        # Reset the pallete
        stroke(0)
        fill(127)

        # Draw the Oscillator
        line(0, 0, x, y)
        circle(x, y, 32)

        # Revert back to the previous p5 canvas state
        pop()


# Initialize a global array containing all oscillators
oscillators = []
for _ in range(NUMBER_OF_OSCILLATORS):
    new_oscillator = Oscillator()
    oscillators.append(new_oscillator)


def draw():
    """
    Draw a single frame on the p5 canvas.
    """
    # Pull in the global oscillators array
    global oscillators

    # Reset the p5 canvas
    background(255) # White

    # Update each oscillator's position then draw it
    for oscillator in oscillators:
        oscillator.update()
        oscillator.show()


# Run the p5 program
run()
