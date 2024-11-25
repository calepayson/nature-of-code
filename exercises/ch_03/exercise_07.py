from p5 import *


# Adjust amplitude and period of the bob
AMPLITUDE = height / 2
PERIOD = 120


def draw():
    """
    Draw a single frame on the p5 canvas.
    """
    # Pull in the global time variable
    global ty

    # Reset the p5 canvas
    background(255) # White

    # Calculate the x value
    x = width / 2
    
    # Calculate the y value
    y = (height / 2) + (AMPLITUDE * sin(TWO_PI * frame_count / PERIOD))

    # Reset the pallet
    stroke(0)
    fill(127)

    # Draw the objects
    line(x, 0, x, y)
    circle(x, y, 48)


# Run the p5 program
run()
