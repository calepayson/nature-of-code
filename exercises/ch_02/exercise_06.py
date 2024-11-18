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

    global balls

    for ball in balls:
        gravity = Vector(0, 1)
        ball.apply_force(gravity)

        if mouse_is_pressed:
            wind = Vector(0.5, 0)
            ball.apply_force(wind)

        if ball.contact_edge():
            c = 0.1
            friction = ball.velocity
            friction *= -1
            friction.normalize()
            friction *= c
            ball.apply_force(friction)

        ball.check_edges(0.9)
        ball.step()
        ball.show()

run()
