"""
Exercise 1
Create a class "Person" which you initialize with the
person's name. Implement the __str__() method. You should be
able to use it as follows:
jessica = Person("Jessica")
print(jessica)  # prints "Person named Jessica"
"""
from functools import total_ordering

@total_ordering # For using total_ordering we have at least define one of the >, <, <=, >=, ...
class Person:
    def __init__(self, name:str, height:int=0) -> None:
        self.name = name
        self.height = height

# getter and setter
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if len(value) <= 1:
            raise ValueError("The name is too short")
        self._name = name
    
    name = property(get_name, set_name) # Important to make getter and setter protected
    
    def __gt__(self, other) -> bool:
        return self.height > other.height
    
    def __str__(self) -> str:
        return f"Person named {self.name}"

# jessica = Person("Jessica")
# print(jessica)  # prints "Person named Jessica"

"""
Exercise 2
Use your "Person" class from the previous exercise.
Besides a person's name, add also his or her height.
Implement the comparison methods so that you can check if
one person is taller than another. Use it as follows:
jessica = Person("Jessica", 180)
scott = Person("Scott", 175)
print(jessica > scott)  # prints True
"""
jessica = Person("Jessica", 180)
scott = Person("Scott", 175)
print(jessica > scott)  # prints True
