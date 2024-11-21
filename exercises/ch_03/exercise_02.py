from p5 import *

# Adjust the drag
DRAG_COEFFICIENT = 0.99

# Global angle variables
angle = 0
angle_velocity = 0
angle_acceleration = 0.0

def draw():
    """Draw a single frame on the p5 canvas."""
    global angle, angle_velocity, angle_acceleration

    # Erase the canvas
    background(255) # White

    # Update the coordinate plane
    translate(width / 2, height / 2)
    rotate(angle)

    # Draw the baton
    stroke(0)   # Black
    fill(127)   # Gray
    line(-60, 0, 60, 0)
    circle(60, 0, 16)
    circle(-60, 0, 16)

    # Mouse interaction
    if mouse_is_pressed:
        angle_acceleration = 0.001
    else:
        angle_acceleration = 0

    # Update the angle
    angle_velocity += angle_acceleration
    angle_velocity *= DRAG_COEFFICIENT
    angle += angle_velocity


# Run the p5 program
run()
