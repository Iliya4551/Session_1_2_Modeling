
import random
from point import Point

class ColorPoint(Point):  # inheritance
    """
    Represents a point in 2D space with an associated color.
    Inherits from the Point class.
    """

    def __init__(self, x, y, color):
        """
        Initializes a ColorPoint with x and y coordinates and a color.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.
            color (str): The color associated with the point.
        """
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        """
        Returns a formatted string representation of the ColorPoint.

        Returns:
            str: The point's color and coordinates in string format.
        """
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1, 2, "red")
print(p)
colors = ["red", "green", "blue", "yellow", "black", "magenta", "cyan",
          "white", "burgundy", "periwinkle", "marsala"]


color_points = []
for i in range(10):
    color_points.append(
        ColorPoint(random.randint(-10, 10),
                   random.randint(-10, 10),
                   random.choice(colors)))


print(color_points)
color_points.sort()
print(color_points)

