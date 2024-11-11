from p5 import *
import random

WIDTH = 640
HEIGHT = 240

class Brush:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2

    def show(self):
        stroke(0)
        point(self.x, self.y)

    def step(self):
        self.x = mouse_x
        self.y = mouse_y

    def splatter(self):
        xoff = random.gauss(0, 10)
        yoff = random.gauss(0, 10)

        no_stroke()
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 50)
        circle((self.x + xoff, self.y + yoff), 5)

brush = Brush()

def setup():
    size(WIDTH, HEIGHT)
    background(204)

def draw():
    brush.step()
    brush.show()
    brush.splatter()

def key_pressed(event):
    background(204)

run()
