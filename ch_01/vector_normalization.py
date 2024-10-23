from p5 import *

def setup():
    size(640, 240)

def draw():
    background(255)

    center = Vector(width, height) / 2
    mouse = Vector(mouse_x, mouse_y)
    drawn_vector = mouse - center

    translate(center.x, center.y)
    stroke(200)
    stroke_weight(4)
    line(0, 0, drawn_vector.x, drawn_vector.y)

    drawn_vector.normalize()
    drawn_vector *= 50
    stroke(0)
    line(0, 0, drawn_vector.x, drawn_vector.y)

run()
