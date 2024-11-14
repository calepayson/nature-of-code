from p5 import *

def setup():
    pass

def draw():
    """Draw a single frame.
    
    Draw three vectors. The third is the result of vector subtraction between 
    the other two. Click to erase the screen.
    """
    # Define each vector
    origin = Vector(0, 0)
    center = Vector(width / 2, height / 2)
    mouse = Vector(mouse_x, mouse_y)
    new_vector = mouse - center

    # Clear the screen if mouse is pressed
    if mouse_is_pressed:
        background(255)

    # Draw the first two vectors
    stroke(200)     # Light gray
    stroke_weight(4)
    line(origin.x, origin.y, center.x, center.y)
    line(origin.x, origin.y, mouse.x, mouse.y)

    # Move the origin to the center of the screen and draw the third vector
    stroke(0)       # Black
    translate(width / 2, height / 2)
    line(origin.x, origin.y, new_vector.x, new_vector.y)
    
# Run the p5 program
run()
