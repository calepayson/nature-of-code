from p5 import *

def setup():
    size(640, 240)

def draw():
    background(255)
    translate(width / 2, height / 2)

    mouse = Vector(mouse_x - (width / 2), mouse_y - (height / 2))

    stroke(200)
    stroke_weight(4)
    line(0, 0, mouse.x, mouse.y)

    mouse *= .5
    stroke(0)
    line(0, 0, mouse.x, mouse.y)

run()
