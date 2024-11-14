from p5 import *

position = Vector(100, 100)
velocity = Vector(1, 3.3)

def setup():
    pass

def draw():
    background(255)
    
    global position, velocity
    position += velocity

    if 0 > position.x or position.x > width:
        velocity.x *= -1
    if 0 > position.y or position.y > height:
        velocity.y *= -1

    stroke(0)
    fill(127)
    circle(position.x, position.y, 48)

run()
