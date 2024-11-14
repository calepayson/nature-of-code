# Nature of Code Workbook

## Layout

- archive/ - Holds old exercises and workbooks.
- exercises/ - Holds the most up to date exercise solutions.
- one_offs/ - Holds one-off programs.
- workbook.py - The current workbook I'm using.

## P5 Learnings

[Link to the documentation](https://p5.readthedocs.io/en/latest/reference/index.html)

**Basic Structure:**
```python
# Import the p5 library
from p5 import *

def setup():
    """Set up the p5 canvas"""
    size(640, 240)      # Set the base size of the canvas
    background(255)     # Set the background color to white (255)

def draw():
    """Draw a single frame on the canvas.

    This is where the meat of the logic goes
    """

# Run the p5 program
run()
```

**Notes**
- width and height are environment variables that represent the window width
  and height. Super useful! Your IDE may complain about them being undefined.
  Tough tiddies, it'll get over it.
- If prompted to use the map() function by the textbook use remap() instead. 
  remap() takes a float and two tuples. The first tuple defines the starting
  range and the second defines the range to map the function to.
- mouse_x, mouse_y, and mouse_is_pressed are useful environmental variables
  when trying to take mouse input.
- The p5 docs state that the circle function take parameters x, y, and radius.
  This is false. Use circle(x, y, diameter).
