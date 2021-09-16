"""
Exercise 1.
Create a new class called "Person", with two variables: name & age.
When you have created your class, you should be able to use it as follows:
p1 = Person("John", 42)
print(p1.name)
print(p1.age)
"""
class Person:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age

p1 = Person("John", 42)
print(p1.name)
print(p1.age)
        

"""
# Exercise 2
Implement a method called "say_hello()".
You should be able to use it as follows:
p1 = Person("John", 42)
p1.say_hello()  # prints "John says hello"
"""
class Person:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"{self.name} says hello")

p1 = Person("John", 42)
p1.say_hello()  # prints "John says hello"