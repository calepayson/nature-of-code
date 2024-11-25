from p5 import *


# Adjust the period and speed
PERIOD = 0.2
SPEED = 0.02


# Initialize global variables
start_angle = 0
delta_angle = PERIOD

def draw():
    """
    Draw a single frame on the p5 canvas.
    """
    # Pull in the global variables
    global start_angle, delta_angle

    # Reset the canvas
    background(255) # White

    # Start at the right y coordinate
    angle = start_angle

    # For each circle...
    for x in range(0, width, 24):
        # Calculate the y coordinate
        y = ((sin(angle) + 1) / 2) * height

        # Reset the pallete
        stroke(0)
        fill(127, 127)

        # Draw the circle
        circle(x, y, 48)

        # Increment the angle
        angle += delta_angle

    # Increment the start angle
    start_angle += SPEED


# Run the p5 program
run()
