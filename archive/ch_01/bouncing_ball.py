from p5 import *

WIDTH = 640
HEIGHT = 240

x = 100
y = 100
xspeed = 2.5
yspeed = 2

def setup():
    size(WIDTH, HEIGHT)

def draw():
    global x, y, xspeed, yspeed

    background(255)

    x += xspeed
    y += yspeed

    if x > width or x < 0:
        xspeed *= -1
    if y > height or y < 0:
        yspeed *= -1

    stroke(0)
    fill(127)
    circle(x, y, 48)

run()
