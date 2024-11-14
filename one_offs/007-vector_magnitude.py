from p5 import *

# The distance in pixels between the magnitude indicator and the edge of the 
# window
PADDING = 8

def draw():
    """Draws a single frame on the p5 canvas

    Draws a vector originating at the center of the screen and ending at the 
    mouse. Draws a rectangle who's length varies to match the magnitude of the 
    vector.
    """
    background(255)     # White

    # Initialize the mouse vector
    center = Vector(width / 2, height / 2)
    mouse = Vector(mouse_x, mouse_y)
    mouse -= center

    # Draw the magnitude bar
    rect(PADDING, PADDING, mouse.magnitude, 8)

    # Translate the origin to the center of the screen
    translate(width / 2, height / 2)
    origin = Vector(0, 0)

    # Draw the vector
    stroke(0)   # Black
    stroke_weight(2)
    line(origin.x, origin.y, mouse.x, mouse.y)

# Run the p5 program
run()
