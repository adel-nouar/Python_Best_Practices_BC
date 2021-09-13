"""
Demo documentation (docstrings) --> Describe what generally is done by the module, the function, etc... It's placed at the top
1) Module level docstring
2) function docstring
3) class docstring
"""

# Comment

def multiply(x: int, y: int):
    """Return the product of x and y."""
    return x * y

print(multiply.__doc__)


class Rectangle:
    """A class used to represent a rectangle shape."""

    def __init__(self, width: float, length: float) -> None:
        self.width = width
        self.length = length

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.length