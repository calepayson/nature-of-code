from p5 import *

def draw():
    """Draw a single frame on the p5 canvas

    Draws two vectors originating from the center of the window. One vector 
    represents the difference between the center and the mouse. The other
    represents half the first vector.
    """
    background(255)     # White

    # Initalize the mouse vector
    mouse = Vector(mouse_x, mouse_y)
    center = Vector(width / 2, height / 2)
    mouse -= center

    # Translate the origin to the center of the screen
    translate(width / 2, height / 2)
    origin = Vector(0, 0)

    stroke(200)     # Light gray
    stroke_weight(2)
    line(origin.x, origin.y, mouse.x, mouse.y)

    stroke(0)   # Black
    stroke_weight(4)
    # Modify the vector
    new_vector = mouse * 0.5
    line(origin.x, origin.y, new_vector.x, new_vector.y)


# Run the p5 program
run()
