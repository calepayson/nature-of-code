from p5 import *

velocity = Vector(2.5, 2)

def setup():
    global position
    size(640, 240)
    position = Vector(width / 2, height / 2)

def draw():
    background(255)

    global position, velocity

    position += velocity

    if position.x > width or position.x < 0:
        velocity.x *= -1
    if position.y > height or position.y < 0:
        velocity.y *= -1

    stroke(0)
    fill(127)
    circle(position.x, position.y, 48)


run()
