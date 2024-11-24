from p5 import *


# Initialize global variables
r = height * 0.45
theta = 0

def draw():
    """
    Draw a single frame on the p5 canvas.
    """
    # Pull in the global variables
    global r, theta

    # Reset the background
    background(255) # White

    # Set the origin to the center of the screen
    translate(width / 2, height / 2)

    # Get a unit vector from theta then scale it by r
    position = Vector.from_angle(theta)
    position *= r

    # Set the pallet and draw the objects
    stroke(0)
    fill(127)
    line(0, 0, position.x, position.y)
    circle(position.x, position.y, 48)

    # Increment theta to produce rotation
    theta += 0.02


# Run the p5 program
run()
