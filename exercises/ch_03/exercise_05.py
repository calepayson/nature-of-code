from p5 import *

PEN_WEIGHT = 15

CHANGE_IN_RADIUS = 0.1
CHANGE_IN_THETA = 0.02

# Initialize global variables
r = 0
theta = 0

def draw():
    """
    Draw a single frame on the p5 canvas.
    """
    # Pull in the global variables
    global r, theta

    # Set the origin to the center of the screen
    translate(width / 2, height / 2)

    # Get a unit vector from theta then scale it by r
    position = Vector.from_angle(theta)
    position *= r

    # Set the pallet and draw the object
    stroke(0)
    fill(0)
    circle(position.x, position.y, PEN_WEIGHT)

    # Increment r and theta before drawing the next frame
    r += CHANGE_IN_RADIUS
    theta += CHANGE_IN_THETA


# Run the p5 program
run()
