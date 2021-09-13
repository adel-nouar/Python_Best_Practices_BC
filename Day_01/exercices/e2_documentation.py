"""
Add 'docstrings' to the following functions and classes.
Follow PEP 257: https://www.python.org/dev/peps/pep-0257/
"""


# 1
import string


def square(n:int):
    """Return the square of r."""
    return n * n


# 2
def count_vowels(word:string):
    """ Return the total number of vowels"""
    number_of_vowels = 0
    for char in word.lower():
        if char in "aeiou":
            number_of_vowels += 1
    return number_of_vowels


# 3
class Dog:
    """A class to represent a dog."""

    def __init__(self, name:string):
        self.name = name

    def bark(self):
        """Make the dog bark."""
        print(f"{self.name} says whoof!")
