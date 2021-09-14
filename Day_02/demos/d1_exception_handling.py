"""
Demo Exception handling
https://docs.python.org/3/library/exceptions.html
"""


try:
    print (1 / 0)
except ZeroDivisionError: # Always add the type of error to manage
    print('Not divisible by 0')


# Always manage exceptions with user input
# Ask for user input
number = input("Give me a number please ") # Not wrapping to an integer
print(number * 2) # The result will be concatenation

# Again but cast to integer
number = int(input("Give me a number please ")) # If the user enter a string like "two" it'll be an error
print(number * 2) 

# Exception handling for user input
try:
    number = int(input("Give me a number please "))
    print(100 / number)
except ValueError: # If the user enter 0, it'll throw another error that we haven't manage
    print("Not a valid number")

# Exception managing ValueError and ZeroDivisionError
try:
    number = int(input("Give me a number please "))
    print(100 / number)
except ValueError:
    print("Not a valid number")
except ZeroDivisionError: 
    print('Not divisible by 0')

# Exception managing all kind of Exception with last condition
try:
    number = int(input("Give me a number please "))
    print(100 / number)
except ValueError:
    print("Not a valid number")
except ZeroDivisionError: 
    print('Not divisible by 0')
except Exception as err: 
    print(err)


# Exception with finally that always be executed
try:
    number = int(input("Give me a number please "))
    print(100 / number)
except ValueError:
    print("Not a valid number")
except ZeroDivisionError: 
    print('Not divisible by 0')
except Exception as err: 
    print(err)
finally:
    print('closing the database connection')


# Custom exceptions (creating our own)
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""


try:
    number = int(input("Give me a number please "))
    if number < 0:
        raise NegativeNumberError
except NegativeNumberError:
    print("Number cannot be negative")