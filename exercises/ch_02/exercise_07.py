from p5 import *
from ball import Ball
import random

balls = []

def setup():
    """Initialize the p5 canvas"""
    global balls

    position_1 = Vector(random.randint(0, width), random.randint(0, height))
    position_2 = Vector(random.randint(0, width), random.randint(0, height))

    diameter_1 = random.randint(20, 60)
    diameter_2 = random.randint(20, 60)

    ball_1 = Ball(position_1, diameter_1)
    ball_2 = Ball(position_2, diameter_2)

    balls.append(ball_1)
    balls.append(ball_2)

def draw():
    """Draw a single frame on the p5 canvas."""
    background(255)     # White

    # Pull in the global objects
    global balls

    for ball in balls:
        # Apply gravity
        gravity = Vector(0, 1)
        ball.apply_force(gravity)

        # If the mouse is pressed
        if mouse_is_pressed:
            mouse = Vector(mouse_x, mouse_y)
            within_x = (
                mouse.x >= ball.position.x - ball.radius and
                mouse.x <= ball.position.x + ball.radius)
            within_y = (
                mouse.y >= ball.position.y - ball.radius and
                mouse.y <= ball.position.y + ball.radius)
            if within_x and within_y:
                ball.velocity = mouse - ball.position

        # If the ball is touching the bottom of the screen, apply friction
        if ball.contact_edge():
            c = 0.1
            friction = ball.velocity
            friction *= -1
            friction.normalize()
            friction *= c
            ball.apply_force(friction)

        # Check the edges, update the position, and draw the ball.
        ball.check_edges(0.9)
        ball.step()
        ball.show()


# Run the p5 program
run()
