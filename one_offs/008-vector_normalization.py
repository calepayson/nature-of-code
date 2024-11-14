from p5 import *

def draw():
    """Draws a single frame on the p5 canvas

    Draws two vectors. One originates from the center of the window and 
    terminates at the mouse. The other is the unit vector of the first.
    """
    background(255)     # White

    # Initialize the mouse vector
    center = Vector(width / 2, height / 2)
    mouse = Vector(mouse_x, mouse_y)
    mouse -= center

    # Translate the origin to the center of the screen
    translate(width / 2, height / 2)
    origin = Vector(0, 0)

    # Draw the first vector
    stroke(200)     # Light gray
    stroke_weight(2)
    line(origin.x, origin.y, mouse.x, mouse.y)

    # Draw the second vector
    stroke(0)
    stroke_weight(4)
    unit_vector = mouse.normalize() * 10    # Multiply by ten for asthetics
    line(origin.x, origin.y, unit_vector.x, unit_vector.y)

# Run the p5 program
run()

