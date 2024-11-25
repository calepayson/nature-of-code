from p5 import *


# Adjust the amplitude and period
AMPLITUDE = width / 3
PERIOD = 120

# Initialize a global variable to keep track of time
tx = 0.0

def draw():
    """
    Draw a single frame on the p5 canvas.
    """
    # Pull in the global time variable
    global tx

    # Reset the canvas
    background(255) # White

    # Calculate the x value of the ball
    x = sin((tx / PERIOD) * 2 * PI) * AMPLITUDE

    # Reset the pallet
    stroke(0)
    fill(127)

    # Move the origin to the center of the screen
    translate(width / 2, height / 2)

    # Draw the objects
    line(0, 0, x, 0)
    circle(x, 0, 48)

    # Increment time
    tx += 1


# Run the p5 program 
run()
