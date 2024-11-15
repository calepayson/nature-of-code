import math

class Vector:
    """Represents a 2D vector.

    Attributes:
        x (float): The x coordinate of the vector.
        y (float): The y coordinate of the vector.
        magnitude(float): The magnitude of the vector.
    """
    def __init__(self, x, y):
        """Constructs a new vector.

        Args:
            x (float): The x coordinate of the vector.
            y (float): The y coordinate of the vector.

        Returns:
            Vector: A new vector object.
        """
        self.x = x
        self.y = y
        self.magnitude = math.sqrt(x ** 2 + y ** 2)

    def normalize(self):
        """Scale the vector to have a magnitude of one."""
        self.x /= self.magnitude
        self.y /= self.magnitude
        self.magnitude = 1

    def limit(self, max):
        """Limit the vector's magnitude to the given max value."""
        if self.magnitude > max:
            self.normalize()
            self.x *= max
            self.y *= max
            self.magnitude = max
