"""
Demo context manager
"""
from typing import final


file = open("zen.txt", "a")
file.write("Simple is better than complex")
file.close()
print(file.closed)


# Better
file = open("zen.txt", "a")
try:
    file.write("Simple is better than complex")
finally:
    file.close()
print(file.closed)

# Best
with open("zen.txt", "a") as file:
    file.write("Simple is better than complex")
print(file.closed)



# Custom context manager
class DemoContextManager:
    def __enter__(self):
        print("Entering the context")
    
    def __exit__(self, *args):
        print("Exiting the context")

with DemoContextManager():
    print("Hello from withing the with statement")


# Using standard library
from contextlib import contextmanager

@contextmanager
def my_open(filename):
    file = open(filename)
    try:
        yield file
    finally:
        file.close()

with my_open("zen.txt") as f:
    print(f.read())