from p5 import *
import random

def draw():
    """Draw a frame on the p5 canvas

    Each frame is a circle at some point along a normal distribution of the x
    axis.
    """
    # Get a random value from a normal distribution
    x = random.gauss(width / 2, width / 10)

    # Draw the circle
    no_stroke()                 # No border
    fill(0, 10)                 # Black, 10% opacity
    circle(x, height / 2, 16)   # x, y, radius

run()
