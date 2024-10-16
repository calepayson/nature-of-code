from p5 import *
import random

def setup():
    size(640, 240)
    background(244)

def draw():
    x = random.gauss(320, 60)
    no_stroke()
    fill(0, 10)
    circle(x, 120, 16)

run()
