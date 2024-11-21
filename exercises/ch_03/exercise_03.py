from p5 import *
from objects import Mover


# Adjust the expected screen width and height (p5 sets up before the screen
# resizes)
SYSTEM_WIDTH = 930
SYSTEM_HEIGHT = 500

# Adjust Cannon width, height, angle, and position
CANNON_WIDTH = 80
CANNON_HEIGHT = 40
CANNON_ANGLE = -1 * PI / 4
CANNON_X = 20
CANNON_Y = SYSTEM_HEIGHT - 40

# Adjust force of cannon
CANNON_FORCE = 100

# Adjust gravity
GRAVITY = 1

# Adjust drag
DRAG_COEFFICIENT = 0.99

# Adjust bounce
BOUNCE_COEFFICIENT = 0.9

countdown = 10

mover_position = Vector(CANNON_X + (CANNON_HEIGHT * sqrt(2) / 2), CANNON_Y)
mover_mass = 2.5
mover = Mover(mover_position, mover_mass)

def draw():
    global countdown, mover

    # Erase the canvas
    background(255) # White

    # Fire the cannon when countdown is zero
    if countdown == 0:
        direction = Vector(sin(CANNON_ANGLE), cos(CANNON_ANGLE))
        force = CANNON_FORCE * direction
        mover.apply_force(force)
    countdown -= 1

    # Apply gravity
    gravity = Vector(0, GRAVITY)
    mover.apply_force(gravity)

    # Update the mover's position
    mover.update()
    # Apply drag
    mover.velocity *= DRAG_COEFFICIENT
    mover.check_edges(BOUNCE_COEFFICIENT)

    # Draw the mover
    mover.show()

    # Draw the cannon
    stroke(0)   # Black
    fill(0)     # Black
    push()
    translate(CANNON_X, CANNON_Y)
    rotate(CANNON_ANGLE)
    rect(0, 0, CANNON_WIDTH, CANNON_HEIGHT)
    pop()


# Run the p5 program
run()
