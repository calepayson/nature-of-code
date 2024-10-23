from p5 import *
import random

WIDTH = 640
HEIGHT = 240

random_counts = []
total = 20

def setup():
    size(WIDTH, HEIGHT)
    for _ in range(total):
        random_counts.append(0)

def draw():
    background(255)
    index = random.randint(0, len(random_counts) - 1)
    random_counts[index] += 1
    stroke(0)
    fill(127)
    w = WIDTH / len(random_counts)
    for x in range(len(random_counts)):
        rect(x * w, HEIGHT - random_counts[x], w - 1, random_counts[x])


if __name__ == "__main__":
    run()
