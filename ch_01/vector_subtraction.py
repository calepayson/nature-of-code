from p5 import *

def setup():
    size(640, 240)
    
def draw():
    global origin, center
    background(255)

    mouse = Vector(mouse_x, mouse_y)
    center = Vector(width / 2, height / 2)

    stroke(200)
    stroke_weight(4)
    line(0, 0, mouse.x, mouse.y)
    line(0, 0, center.x, center.y)

    mouse -= center

    stroke(0)
    translate(width / 2, height / 2)
    line(0, 0, mouse.x, mouse.y)


run()
