from p5 import *
import random

# Set the space between the slider and its borders
PADDING = 16

class PaintBrush:
    """Represents a paintbrush that splatters paint at the mouse location

    Attributes:
        x (int): The x coordinate of the paintbrush
        y (int): The y coordinate of the paintbrush
        splatter_distance (int): The standard deviation of splatter
    """
    def __init__(self):
        """Initializes a paintbrush"""
        self.x = width / 2
        self.y = height / 2
        self.splatter_distance = 10

    def update_splatter_distance(self, new_distance: int):
        """Updates the splatter distance

        Arguments:
            new_distance (int): The updated standard deviation of splatter
        """
        self.splatter_distance = new_distance

    def step(self):
        """Updates the location of the paintbrush to match the mouse"""
        self.x = mouse_x
        self.y = mouse_y

    def show(self):
        """Draws a frame of splatter

        Splatter happens along a normal distribution starting from the location
        of the mouse. Color is chosen from a normal distribution of red, green,
        and blue values.
        """
        splatter_x = random.gauss(self.x, self.splatter_distance)
        splatter_y = random.gauss(self.y, self.splatter_distance)
        color = Color(
            r = random.gauss(127, 50),
            g = random.gauss(127, 50),
            b = random.gauss(127, 50))
        stroke(color)
        fill(color)
        circle(splatter_x, splatter_y, 3)

class Slider:
    """Represents a slider

    Attributes:
        value (float): The value that the slider is at
        max (int): The maximum value of the slider
        size (int): The size in pixels of the slider icon
    """
    def __init__(self):
        """Initializes a slider object"""
        self.value = 10
        self.max = 25
        self.size = 16

    def update(self):
        """Updates the slider if the mouse is pressed within the slider bar"""
        # If the mouse is pressed within the slider bar...
        if mouse_is_pressed and PADDING <= mouse_y <= self.size + PADDING:
            # Set the value of the slider to the relative proportion of max
            self.value = self.max * mouse_x / width

    def show(self):
        """Draws a single frame of the slider"""
        # Draw the background
        fill(255)   # White
        stroke(255) # White
        rect(0, 0, width, PADDING * 2 + self.size)  # x1, y1, x2, y2

        # Draw the slider bar
        stroke(0)   # Black
        line(0, PADDING + (self.size / 2), width, PADDING + (self.size / 2))    # x1, y1, x2, y2

        # Draw the slider icon
        x = self.value * width / self.max   # Convert value to a portion of width
        y = PADDING + (self.size / 2)       # Set at proper height
        circle(x, y, self.size)             # Draw the icon


# Initialize the paintbrush and slider global variables
global paintbrush, slider

def setup():
    """Set up the p5 canvas"""
    # Set size and background color
    size(640, 240)
    background(255)

    # Update the global variables to new objects
    global paintbrush, slider
    paintbrush = PaintBrush()
    slider = Slider()

def draw():
    """Draw a single frame on the p5 canvas"""

    # pull in the global objects
    global paintbrush, slider

    # Update the slider values if needed and show the slider
    slider.update()
    slider.show()

    # Update the paintbrush with the slider values and mouse position and draw 
    # a new frame
    paintbrush.update_splatter_distance(slider.value)
    paintbrush.step()
    paintbrush.show()


# Run the p5 program
run()
