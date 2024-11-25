from p5 import *
import random

# Adjust distance between wave nodes
STEP = 20

# Adjust the speed at which the wave moves
SPEED = 10

# Adjust the number of waves
NUMBER_OF_WAVES = 3

# Adjust min and max period
MIN_PERIOD = 300
MAX_PERIOD = 750

# Adjust min and max amplitude
MIN_AMPLITUDE = 30
MAX_AMPLITUDE = 150

class Wave:
    """
    A generic representation of a wave.

    Attributes:
        period (int): The period of the wave in pixels.
        amplitude (int): The amplitude of the wave in pixels.
    """
    def __init__(self, period: int, amplitude: int):
        """
        Construct a new Wave object.

        Args:
            period (int): The period of the wave in pixels.
            amplitude (int): The amplitude of the wave in pixels.
        """
        self.period = period
        self.amplitude = amplitude

    def get_height(self, x):
        """
        Get the height of the wave at a given x position.

        Args:
            x (float): The x coordinate of the desired point.

        Returns: 
            float: The y coordinate of the desired point.
        """
        return sin(TWO_PI * x / self.period) * self.amplitude

# Initialize global variables
start = 0
waves = []


# Initalize all wave objects
for _ in range(NUMBER_OF_WAVES):
    period = random.randint(MIN_PERIOD, MAX_PERIOD)
    amplitude = random.randint(MIN_AMPLITUDE, MAX_AMPLITUDE)
    wave = Wave(period, amplitude)
    waves.append(wave)

def draw():
    """
    Draw a single frame on the p5 canvas.
    """
    # Pull in the global variables (necessary for p5)
    global waves, start

    # Reset the canvas
    background(255) # White

    # For every circle...
    for x in range(0, width, STEP):
        # Set the origin of y to the center of the screen
        y = height / 2

        # Add up the amplitudes of each wave at x
        for wave in waves:
            y += wave.get_height(x + start)

        # Reset the pallete
        stroke(0)       # Black
        fill(127, 127)  # Gray, 50% opacity

        # Draw the circle
        circle(x, y, 48)

    # Increment the starting position
    start += SPEED


# Run the p5 program
run()
