"""
Demo decorators : We could extends functionalities to a function
We could add many decorators for a single function, but best practices to keep at as simple as possible (simple is better than complex)
"""

# Example function 
def say_hello():
    print("Hello, how are you?")


# 1. Functions as objects
# greet = say_hello()
# greet()

# 2. Functions as arguments
def my_simple_decorator(func):
    print("Decorating the function")
    func()

# my_simple_decorator(say_hello)


# 3. Docorator
def my_decorator(func):
    def wrapper():
        print("Before calling the decorated function")
        func() # Here the function is called
        print("After calling the decorated function")
    return wrapper()

# say_hello = my_decorator(say_hello)

@my_decorator # -> Those lines are equivalents to say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello, how are you?")


@my_decorator
def say_goodbye():
    print("Bye, bye")
