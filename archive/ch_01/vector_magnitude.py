from p5 import *

def setup():
    size(640, 240)

def draw():
    background(255)
    center = Vector(width / 2, height / 2)
    mouse = Vector(mouse_x, mouse_y)

    stroke(0)
    stroke_weight(4)
    line(center.x, center.y, mouse.x, mouse.y)

    drawn_vector = mouse - center

    stroke(0)
    stroke_weight(30)
    line(10, 10, 10 + float(drawn_vector.mag()), 10)

run()
